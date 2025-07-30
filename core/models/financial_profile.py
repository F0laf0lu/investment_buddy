import uuid
from django.db import models
from django.conf import settings
from .base_model import BaseModel

class FinancialProfile(BaseModel):
    """
    Creates a model for the Financial Profile of a user
    """
    RISK_APPETITE_CHOICES = [
        ('low', 'LOW'), ('medium', 'MEDIUM'), ('high', 'HIGH')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='financial_profile')
    monthly_income = models.PositiveIntegerField(null=True, blank=True)
    risk_appetite = models.CharField(max_length=50, choices=RISK_APPETITE_CHOICES, null=True, blank=True)
    investment_budget = models.PositiveIntegerField(null=True, blank=True)
    maximum_principal = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Financial profile for {self.user.email}"