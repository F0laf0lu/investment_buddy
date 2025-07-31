from rest_framework import serializers
from ..models.investment_portfolio import InvestmentPortfolio


class InvestmentPortfolioSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = InvestmentPortfolio
        fields = [
            'id', 'product', 'product_name', 'amount_invested',
            'date_invested', 'status', 'units_purchased', 'expected_yield',
            'holding_period_days', 'remaining_units'
        ]