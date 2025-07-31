from django.urls import path
from ..views.wallet import WalletCreateView, WalletDetailView, WalletUpdateView

urlpatterns = [
    path('wallet/', WalletCreateView.as_view(), name='wallet-create'),
    path('wallet/update/', WalletUpdateView.as_view(), name='wallet-update'),
    path('wallet/detail/', WalletDetailView.as_view(), name='wallet-detail'),
]