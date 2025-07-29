import uuid
from django.db import models
from .base_model import BaseModel

class InvestmentProduct(BaseModel):

    RISK_LEVEL_CHOICES = [
        ('LOW', 'LOW'), 
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),       
    ]

    ASSET_TYPES = [
        ('MUTUAL_FUNDS', 'Mutual Funds'),
        ('TREASURY_BILLS', 'Treasury Bills'),
        ('NAIRA_BONDS', 'Naira Bonds'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    asset_type = models.CharField(max_length=50, choices=ASSET_TYPES, null=True, blank=True)
    asset_type_description = models.TextField(blank=True, null=True)
    image = models.URLField(max_length=200, blank=True, null=True)
    risk_level = models.CharField(max_length=50, choices=RISK_LEVEL_CHOICES, null=True, blank=True)
    bid_price = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    offer_price = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    indicative_yield = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    prospectus_url = models.URLField(max_length=200, blank=True, null=True)
    min_investment = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    min_holding_days = models.PositiveIntegerField(help_text="Minimum holding period in days", null=True, blank=True)
    min_subsequent_investment = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    thirty_day_yield_change = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    one_year_yield_change = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    year_to_date_yield_change = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    five_year_yield_change = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    historical_data = models.JSONField(blank=True, null=True, help_text="Historical data for the investment product")

    def __str__(self):
        return self.name



