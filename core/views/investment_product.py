from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from ..models.investment_product import InvestmentProduct
from ..serializers.investment_product_serializer import InvestmentProductSerializer, InvestmentProductDetailSerializer

class InvestmentProductListView(generics.ListAPIView):
    queryset = InvestmentProduct.objects.all()
    serializer_class = InvestmentProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['asset_type', 'risk_level']
    search_fields = ['name', 'description', 'asset_type']


class InvestmentProductDetailView(generics.RetrieveAPIView):
    queryset = InvestmentProduct.objects.all()
    serializer_class = InvestmentProductDetailSerializer
    lookup_field = 'id'

