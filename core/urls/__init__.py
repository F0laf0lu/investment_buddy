from django.urls import path, include

urlpatterns = [
    path('', include('core.urls.investment_product')),
    path('', include('core.urls.financial_profile')),
    path('', include('core.urls.chatbot')),
    path('', include('core.urls.transaction')),
    path('', include('core.urls.investment_portfolio')),
    path('', include('core.urls.wallet')),
    path('', include('core.urls.dashboard'))
]