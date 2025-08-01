from rest_framework import generics, status, permissions
from ..models.investment_product import InvestmentProduct
from ..serializers.investment_product_serializer import InvestmentProductSerializer
from ..utils.chatbot_response import InvestmentChatBot
from ..utils.response import Response


class ChatBotView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = InvestmentProductSerializer

    def post(self, request, *args, **kwargs):
        user_message = request.data.get("message", "")

        if not user_message:
            return Response(
                success=False,
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Message is required",
                errors={'error': "Missing user input"}
            )

        chatbot = InvestmentChatBot()
        response_data = chatbot.get_response(user_message)
        filters = response_data.get("filters", {})

        queryset = InvestmentProduct.objects.filter(**filters)

        serializer = self.get_serializer(queryset, many=True)

        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message=response_data.get("message"),
            data=serializer.data
        )