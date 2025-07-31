from rest_framework import permissions, status, generics
from ..utils.response import Response
from ..models.investment_portfolio import InvestmentPortfolio
from ..serializers.investment_portfolio_serializer import InvestmentPortfolioSerializer


class InvestmentPortfolioCreateView(generics.CreateAPIView):
    serializer_class = InvestmentPortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                success = True,
                status_code=status.HTTP_201_CREATED,
                message='Portfolio created successfully',
                data=serializer.data
            )
        return Response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            errors=serializer.errors,
            message='Unsuccessful Portfolio Creation'
        )

class InvestmentPortfolioUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InvestmentPortfolioSerializer
    lookup_field = 'id'

    def get_queryset(self):
        portfolio = InvestmentPortfolio.objects.filter(user=self.request.user)
        return portfolio

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                success = True,
                status_code=status.HTTP_200_OK,
                message='Portfolio updated successfully',
                data=serializer.data
            )
        return Response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            errors=serializer.errors,
            message='Unsuccessful Portfolio Update'
        )

class InvestmentPortfolioDetailView(generics.RetrieveAPIView):
    serializer_class = InvestmentPortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        portfolio = InvestmentPortfolio.objects.filter(user=self.request.user)
        return portfolio

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message="Investment Portfolio successfully retrieved",
            data=serializer.data
        )


class InvestmentPortfolioListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InvestmentPortfolioSerializer

    def get_queryset(self):
        portfolio = InvestmentPortfolio.objects.filter(user=self.request.user)
        return portfolio

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                status_code=status.HTTP_404_NOT_FOUND,
                success=False,
                message='Portfolios not found',
                data=[]
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(
            status_code=status.HTTP_200_OK,
            success=True,
            message='All portfolios listing for user',
            data=serializer.data
        )