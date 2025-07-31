from django.urls import path
from ..views.dashboard import DashboardView


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='user-dashboard'),
]