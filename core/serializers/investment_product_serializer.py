from rest_framework import serializers
from ..models.investment_product import InvestmentProduct

class InvestmentProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentProduct
        fields = '__all__'