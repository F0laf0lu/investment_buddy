from django.db import models
from .base_model import BaseModel

class InvestmentProduct(BaseModel):
    """
    Creates the model class for the Investments Products
    """
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    description = models.TextField()
    interest_rate = models.FloatField()
    category = models.CharField(max_length=50)
    min_allowed_amt = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} at {self.interest_rate}"
