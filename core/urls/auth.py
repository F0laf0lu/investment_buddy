from django.urls import include, path
from core.views.auth import RegisterUserView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register', RegisterUserView.as_view(), name="register-user"),
    path('login', LoginView.as_view(), name="login-user"),
]