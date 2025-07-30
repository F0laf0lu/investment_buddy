from django.urls import path, include

urlpatterns = [
    path('', include('core.urls.investment_product')),
    path('', include('core.urls.financial_profile'))
]