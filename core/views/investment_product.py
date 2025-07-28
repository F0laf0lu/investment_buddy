from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from ..models.investment_product import InvestmentProduct
from ..serializers.investment_product_serializer import InvestmentProductSerializer

class InvestmentProductListView(generics.ListAPIView):
    queryset = InvestmentProduct.objects.all()
    serializer_class = InvestmentProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'type']
    search_fields = ['name', 'description']


class InvestmentProductDetailView(generics.RetrieveAPIView):
    queryset = InvestmentProduct.objects.all()
    serializer_class = InvestmentProductSerializer
    lookup_field = 'id'

