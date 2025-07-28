from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from core.serializers.user_auth import RegisterUserSerializer
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
            status_code=status.HTTP_201_CREATED,
            success=True,
            data=serializer.data,
            message="User registered successfully."
        )