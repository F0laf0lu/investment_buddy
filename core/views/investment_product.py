from rest_framework import generics, filters, status, permissions
from ..utils.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ..models.investment_product import InvestmentProduct
from ..serializers.investment_product_serializer import InvestmentProductSerializer, InvestmentProductDetailSerializer

class InvestmentProductListView(generics.ListAPIView):
    serializer_class = InvestmentProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['asset_type', 'risk_level']
    search_fields = ['name', 'description', 'asset_type']

    def get_queryset(self):
        return InvestmentProduct.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message='Investments found',
            data=serializer.data
        )


class InvestmentProductDetailView(generics.RetrieveAPIView):
    queryset = InvestmentProduct.objects.all()
    serializer_class = InvestmentProductDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message='Investment retrieved successfully',
            data=serializer.data
        )