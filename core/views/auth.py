from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from core.serializers.user_auth import RegisterUserSerializer, LoginSerializer, UserSerializer
from core.utils.response import Response

class RegisterUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status_code=status.HTTP_400_BAD_REQUEST,
                success=False,
                errors=serializer.errors
            )
        self.perform_create(serializer)
        return Response(
            success=True,
            message="User registered successfully.",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED,
        )
    

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                message="Validation error",
                status_code=status.HTTP_400_BAD_REQUEST,
                success=False,
                errors=serializer.errors
            )
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        user = authenticate(email=email, password=password)
        if not user:
            return Response(
                success=False,
                message="Invalid email or password. Try again",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        
        refresh = RefreshToken.for_user(user)
        user_data = UserSerializer(user).data
        return Response(
            message = "Login successful.",
            success=True,
            data={
                    'token': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    },
                    'user': user_data
                },
            status_code=status.HTTP_200_OK,
            )
