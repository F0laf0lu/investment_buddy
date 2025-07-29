from django.urls import path
from ..views.investment_product import InvestmentProductListView, InvestmentProductDetailView

urlpatterns = [
    path('products', InvestmentProductListView.as_view(), name='investment-product-list'),
    path('product/<id>', InvestmentProductDetailView.as_view(), name='investment-product-details'),
]