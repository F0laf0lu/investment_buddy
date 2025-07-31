from rest_framework import serializers
from ..models.financial_profile import FinancialProfile

class FinancialProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialProfile
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at'  ]

    def create(self, validated_data):
        """Create a financial profile for a user"""
        user = self.context['request'].user
        profile = FinancialProfile.objects.create(
            user=user,
            monthly_income = validated_data['monthly_income'],
            risk_appetite = validated_data['risk_appetite'],
            investment_budget = validated_data['investment_budget'],
            maximum_principal = validated_data['maximum_principal'])
        return profile

    def update(self, instance, validated_data):
        """Update a financial profile for a user"""
        validated_data.pop('user', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance