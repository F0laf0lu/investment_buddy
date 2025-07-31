from rest_framework import generics, status, permissions

from ..models.financial_profile import FinancialProfile
from ..models.investment_portfolio import InvestmentPortfolio
from ..models.wallet import Wallet
from ..serializers.financial_profile_serializer import FinancialProfileSerializer
from ..serializers.investment_portfolio_serializer import InvestmentPortfolioSerializer
from ..serializers.wallet_serializer import WalletSerializer
from ..utils.response import Response


class DashboardView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        # Wallet Info
        wallet = Wallet.objects.filter(user=user).first()
        if wallet:
            wallet_data = WalletSerializer(wallet).data
        else:
            wallet_data = None

        # Portfolio
        portfolio = InvestmentPortfolio.objects.filter(user=user)
        if portfolio:
            portfolio_data = InvestmentPortfolioSerializer(portfolio, many=True).data
        else:
            portfolio_data = None

        # Transactions

        # Financial Profile
        profile = FinancialProfile.objects.filter(user=user).first()
        if profile:
            portfolio_data = FinancialProfileSerializer(profile).data
        else:
            portfolio_data = None

        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message='Dashboard data retrieved successfully',
            data={
                "user_profile": user,
                "wallet": wallet_data,
                "portfolio": portfolio_data,
                "transactions": [],
                "financial_profile": []
            }
        )
