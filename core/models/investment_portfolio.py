import uuid
from django.db import models
from django.conf import settings
from ..models.base_model import BaseModel
from ..models.investment_product import InvestmentProduct


class InvestmentPortfolio(BaseModel):
    STATUS = [
        ('active', 'ACTIVE'),
        ('redeemed', 'REDEEMED'),
        ('matured', 'MATURED'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='portfolios')
    product = models.ForeignKey(InvestmentProduct, on_delete=models.CASCADE, related_name='portfolios')
    units_purchased = models.PositiveIntegerField()
    amount_invested = models.DecimalField(max_digits=12, decimal_places=2)
    date_invested = models.DateTimeField(auto_now_add=True)
    expected_yield = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    holding_period_days = models.PositiveIntegerField()
    status=models.CharField(max_length=10, choices=STATUS)
    remaining_units = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.status}"