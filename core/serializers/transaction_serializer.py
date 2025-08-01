from rest_framework import serializers
from ..models.transaction import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id', read_only=True)
    class Meta:
        model = Transaction
        fields = ['id',
                  'transaction_reference',
                  'user_id',
                  'transaction_type',
                  'amount',
                  'status',
                  'description',
                  'created_at',
                  'updated_at',]