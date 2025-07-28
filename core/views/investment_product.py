from rest_framework import generics
from ..models.investment_product import InvestmentProduct
from ..serializers.investment_product_serializer import InvestmentProductSerializer

class InvestmentProductListView(generics.ListAPIView):
    queryset = InvestmentProduct.objects.all()
    serializer_class = InvestmentProductSerializer

class InvestmentProductDetailView(generics.RetrieveAPIView):
    queryset = InvestmentProduct.objects.all()
    serializer_class = InvestmentProductSerializer
    lookup_field = 'id'