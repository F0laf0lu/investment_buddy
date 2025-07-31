from rest_framework import generics, status, permissions
from ..models.transaction import Transaction
from ..serializers.transaction_serializer import TransactionSerializer
from ..utils.response import Response


class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                success = True,
                status_code=status.HTTP_201_CREATED,
                message='Transaction made successfully',
                data=serializer.data
            )
        return Response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            errors=serializer.errors,
            message='Unsuccessful Transaction'
        )

class TransactionDetailView(generics.RetrieveAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        transaction = Transaction.objects.filter(user=self.request.user)
        return transaction

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message="Transaction successfully retrieved",
            data=serializer.data
        )

class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        transaction = Transaction.objects.filter(user=self.request.user)
        return transaction

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                status_code=status.HTTP_404_NOT_FOUND,
                success=False,
                message='No transactions found',
                data=[]
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(
            status_code=status.HTTP_200_OK,
            success=True,
            message='All transactions listing for user',
            data=serializer.data
        )