from rest_framework import serializers
from ..models.investment_product import InvestmentProduct

class InvestmentProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentProduct
        fields = [
            'id',
            'name',
            'description',
            'risk_level',
            'asset_type',
            'asset_type_description',
            'image',
            'bid_price',
            'offer_price',
            'indicative_yield',
        ]


class InvestmentProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentProduct
        fields = [
            'id',
            'name',
            'description',
            'risk_level',
            'asset_type',
            'asset_type_description',
            'image',
            'prospectus_url',
            'bid_price',
            'offer_price',
            'indicative_yield',
            'min_investment',
            'min_holding_days',
            'min_subsequent_investment', 
            'thirty_day_yield_change',
            'one_year_yield_change',
            'year_to_date_yield_change',
            'five_year_yield_change',
            'historical_data',
        ]
