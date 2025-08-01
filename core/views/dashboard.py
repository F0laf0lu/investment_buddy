from rest_framework import generics, status, permissions
from ..models.financial_profile import FinancialProfile
from ..models.investment_portfolio import InvestmentPortfolio
from ..models.transaction import Transaction
from ..models.wallet import Wallet
from ..serializers.financial_profile_serializer import FinancialProfileSerializer
from ..serializers.investment_portfolio_serializer import InvestmentPortfolioSerializer
from ..serializers.transaction_serializer import TransactionSerializer
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
        transactions = Transaction.objects.filter(user=user).order_by('created_at')[:5]
        total_transactions = Transaction.objects.filter(user=user).count()
        transaction_data = TransactionSerializer(transactions, many=True).data

        # Financial Profile
        profile = FinancialProfile.objects.filter(user=user).first()
        if profile:
            profile_data = FinancialProfileSerializer(profile).data
        else:
            profile_data = None

        return Response(
            success=True,
            status_code=status.HTTP_200_OK,
            message='Dashboard data retrieved successfully',
            data={
                "user_profile": {
                    "id": str(user.id),
                    "email": user.email,
                    "full_name": user.full_name
                },
                "wallet": wallet_data,
                "portfolio": portfolio_data,
                "transactions": {
                    "top5_transactions": transaction_data,
                    "total_transactions": total_transactions
                },
                "financial_profile": profile_data
            }
        )
