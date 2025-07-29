from django.contrib import admin
from .models.investment_product import InvestmentProduct
from .models.user import User

# Register your models here.

admin.site.register(InvestmentProduct)
admin.site.register(User)   