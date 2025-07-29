from django.db import models
from django.conf import settings
from .base_model import BaseModel

class FinancialProfile(BaseModel):
    """
    Creates a model for the Financial Profile of a user
    """
    RISK_APPETITE_CHOICES = [
        ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='financial_profile')
    monthly_income = models.PositiveIntegerField()
    risk_appetite = models.CharField(max_length=50, choices=RISK_APPETITE_CHOICES)
    investment_budget = models.PositiveIntegerField()
    maximum_principal = models.PositiveIntegerField()

    def __str__(self):
        return f"Financial profile for {self.user.email}"