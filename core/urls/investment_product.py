from django.urls import path
from ..views.investment_product import InvestmentProductListView, InvestmentProductDetailView, TailoredInvestmentProductListView

urlpatterns = [
    path('products/', InvestmentProductListView.as_view(), name='investment-product-list'),
    path('product/<uuid:id>', InvestmentProductDetailView.as_view(), name='investment-product-details'),
    path('products/foryou/', TailoredInvestmentProductListView.as_view(), name='tailored-investment-product-list')
]