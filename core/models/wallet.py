import uuid
from django.conf import settings
from django.db import models
from ..models.base_model import BaseModel


class Wallet(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallet')
    bank_name = models.CharField(max_length=200)
    bank_account_name = models.CharField(max_length=100)
    bank_account_number = models.IntegerField(unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.email} - {self.bank_account_number}"