from rest_framework import generics, permissions, status
from ..models.wallet import Wallet
from ..serializers.wallet_serializer import WalletSerializer
from ..utils.response import Response


class WalletCreateView(generics.CreateAPIView):
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                success=True,
                status_code=status.HTTP_201_CREATED,
                message="Wallet successfully added",
                data=serializer.data
            )
        return Response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Wallet adding failed",
            error=serializer.errors
        )

class WalletUpdateView(generics.UpdateAPIView):
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        wallet = Wallet.objects.get(user=self.request.user)
        return wallet

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                success=True,
                status_code=status.HTTP_200_OK,
                message="Wallet successfully updated",
                data=serializer.data
            )
        return Response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            message="Wallet update failed",
            error=serializer.errors
        )


class WalletDetailView(generics.RetrieveAPIView):
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        wallet = Wallet.objects.get(user=self.request.user)
        return wallet

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message="Wallet successfully retrieved",
            data=serializer.data
        )