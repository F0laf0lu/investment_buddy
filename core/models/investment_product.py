from django.db import models
from base_model import BaseModel

class InvestmentProduct(BaseModel):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    description = models.TextField()
    interest_rate = models.FloatField()
    category = models.CharField(max_length=50)
    min_allowed_amt = models.PositiveIntegerField()
