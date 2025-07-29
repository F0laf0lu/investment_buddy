from django.urls import path
from ..views.financial_profile import FinancialProfileCreateView, FinancialProfileDetailView, FinancialProfileUpdateView


urlpatterns = [
    path('profile/', FinancialProfileDetailView.as_view(), name='financial_profile_detail'),
    path('profile/me/', FinancialProfileCreateView.as_view(), name='financial_profile_create'),
    path('profile/update/', FinancialProfileUpdateView.as_view(), name='financial_profile_update')
]