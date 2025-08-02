from rest_framework import generics, status, permissions
from django.utils.html import escape
from ..models.financial_profile import FinancialProfile
from ..models.investment_product import InvestmentProduct
from ..serializers.investment_product_serializer import InvestmentProductSerializer
from ..utils.chatbot_response import InvestmentChatBot, RISK_BASED_PROMPTS, PROMPT_TO_RISK_MAP, PROMPT_RESPONSE_MESSAGES
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

        if not queryset.exists():
            return Response(
                success=True,
                status_code=status.HTTP_200_OK,
                message="No matching investments found.",
                data="<p>Sorry, we couldn't find any matching investment products at this time.</p>"
            )

        html_content = [f"<h2>{escape(response_data.get('message', 'Here are some investment suggestions:'))}</h2><ul>"]

        for product in queryset:
            html_content.append(f"""
                <li style="margin-bottom: 1rem;">
                    <h3>{escape(product.name)}</h3>
                    <p><strong>Description:</strong> {escape(product.description)}</p>
                    <p><strong>Asset Type:</strong> {escape(product.asset_type.replace('_', ' ').title())}</p>
                    <p><strong>Risk Level:</strong> {escape(product.risk_level.title())}</p>
                    <p><strong>Yield:</strong> {product.indicative_yield}% &nbsp;&nbsp; <strong>Offer Price:</strong> ₦{product.offer_price:,.2f}</p>
                    <a href="{escape(product.prospectus_url)}" target="_blank">View Prospectus</a>
                </li>
            """)

        html_content.append("</ul>")

        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message=response_data.get("message"),
            data={
                "html": "".join(html_content),
                "investment_products": serializer.data
            }
        )

class ChatbotPromptView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, *args, **kwargs):
        user = request.user
        profile = FinancialProfile.objects.filter(user=user).first()

        if not profile:
            return Response(
                success=False,
                status_code=status.HTTP_404_NOT_FOUND,
                message="User financial profile not found.",
                data=None
            )

        risk_level = profile.risk_appetite
        prompts = RISK_BASED_PROMPTS.get(risk_level.upper(), [])

        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message="Prompts generated successfully",
            data={
                "risk_level": risk_level,
                "prompts": prompts
            }
        )

class ChatbotRespondView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InvestmentProductSerializer

    def post(self, request, *args, **kwargs):
        message = request.data.get("message", "").lower().strip()

        risk_level = PROMPT_TO_RISK_MAP.get(message)
        response_text = PROMPT_RESPONSE_MESSAGES.get(message)

        if not risk_level or not response_text:
            return Response(
                success=False,
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Prompt not recognized or not supported.",
                data="<p>The message provided does not match any of the known prompts.</p>"
            )

        investments = InvestmentProduct.objects.filter(risk_level=risk_level).order_by('-created_at')[:2]
        serializer = self.get_serializer(investments, many=True)
        text_blocks = [
            f"{response_text} ",
            f"Here are some {risk_level.lower()}-risk investments you might consider: "
        ]
        html_blocks = [
            f"<h2>{escape(response_text)}</h2>",
            f"<h3>Here are some <strong>{risk_level.lower()}-risk</strong> investments you might consider:</h3>",
            "<ul>"
        ]

        for inv in investments:
            html_blocks.append(f"""
                <li style="margin-bottom: 1rem;">
                    <h4>{escape(inv.name)}</h4>
                    <p><strong>Description:</strong> {escape(inv.description)}</p>
                    <p><strong>Asset Type:</strong> {escape(inv.asset_type.replace('_', ' ').title())}</p>
                    <p><strong>Yield:</strong> {inv.indicative_yield}% &nbsp;&nbsp; <strong>Offer Price:</strong> ₦{inv.offer_price:,.2f}</p>
                    <a href="{escape(inv.prospectus_url)}" target="_blank">View Prospectus</a>
                </li>
            """)

        html_blocks.append("</ul>")

        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message="Chatbot response generated.",
            data={
                "html": "".join(html_blocks),
                "text": "".join(text_blocks),
                "investment_products": serializer.data
            }
        )