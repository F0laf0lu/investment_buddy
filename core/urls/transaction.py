from django.urls import path
from ..views.transaction import TransactionCreateView, TransactionDetailView, TransactionListView

urlpatterns = [
    path('transaction/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction/all/', TransactionListView.as_view(), name='transaction-user-list'),
    path('transaction/detail/<uuid:id>', TransactionDetailView.as_view(), name='transaction-detail'),
]