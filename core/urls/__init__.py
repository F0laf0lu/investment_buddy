from django.urls import path, include

urlpatterns = [
    path('', include('investment_buddy_be.core.urls.investment_product')),
]