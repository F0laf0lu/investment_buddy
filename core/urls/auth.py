from django.urls import include, path
from core.views.auth import RegisterUserView

urlpatterns = [
    path('', RegisterUserView.as_view(), name="register-user"),
]