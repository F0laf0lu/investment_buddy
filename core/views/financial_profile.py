from rest_framework import generics, permissions, status
from ..utils.response import Response
from ..models.financial_profile import FinancialProfile
from ..serializers.financial_profile_serializer import FinancialProfileSerializer


class FinancialProfileCreateView(generics.CreateAPIView):
    serializer_class = FinancialProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        if FinancialProfile.objects.filter(user=user).exists():
            return Response(
                success=False,
                status_code=status.HTTP_400_BAD_REQUEST,
                errors={'details': 'Financial profile already exists for the user'},
                message='Unsuccessful profile creation'
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                success = True,
                status_code=status.HTTP_201_CREATED,
                message='Financial profile created successfully',
                data=serializer.data
            )
        return Response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            errors=serializer.errors,
            message='Unsuccessful profile creation'
        )

class FinancialProfileUpdateView(generics.UpdateAPIView):
    serializer_class = FinancialProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile = FinancialProfile.objects.get(user=self.request.user)
        return profile

    def post(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                success = True,
                status_code=status.HTTP_200_OK,
                message='Financial profile updated successfully',
                data=serializer.data
            )
        return Response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            errors=serializer.errors,
            message='Unsuccessful profile update'
        )


class FinancialProfileDetailView(generics.RetrieveAPIView):
    serializer_class = FinancialProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile = FinancialProfile.objects.get(user=self.request.user)
        return profile

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(profile)

        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message='Profile found',
            data=serializer.data
        )