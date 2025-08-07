from django.db.models import Sum
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
        portfolio = InvestmentPortfolio.objects.filter(user=user).select_related('product')
        active_investment = portfolio.count()

        total_current_value = 0
        total_invested = 0
        portfolio_data = []

        for p in portfolio:
            bid = p.product.bid_price
            offer = p.product.offer_price
            units = p.units_purchased
            invested = p.amount_invested
            ytd = p.product.year_to_date_yield_change or 0
            current_value = units * offer

            gain_loss = (offer - bid) * units
            gain_loss_percent = (gain_loss / invested) * 100
            ytd_return  = (ytd / 100) * invested

            total_current_value += current_value
            total_invested += invested

            portfolio_data.append({
                "id": p.id,
                "product_name": p.product.name,
                "asset_type": p.product.asset_type,
                "risk_level":p.product.risk_level,
                "amount_invested": invested,
                "units": units,
                "gain_loss_amount": round(gain_loss, 2),
                "gain_loss_percent": round(gain_loss_percent, 2),
                "ytd_percent": ytd,
                "ytd_return_amount": round(ytd_return, 2),
            })

        net_profit = total_current_value - total_invested
        percent_return = net_profit / total_invested * 100

        # Transactions
        total_deposit = Transaction.objects.filter(user=user, transaction_type='DEPOSIT', status='SUCCESS').aggregate(total=Sum('amount'))['total'] or 0
        total_withdrawal = Transaction.objects.filter(user=user, transaction_type='WITHDRAWAL', status='SUCCESS').aggregate(total=Sum('amount'))['total'] or 0
        transactions = Transaction.objects.filter(user=user).order_by('created_at')
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
                "portfolio": {
                    "active_investments": active_investment,
                    "portfolio_value": total_current_value,
                    "net_profit_loss": net_profit,
                    "profit_loss_percent": percent_return,
                    "goal_progress": round((total_invested / total_current_value) * 100),
                    "investment_list": portfolio_data
                },
                "transactions": {
                    "transactions_list": transaction_data,
                    "total_transactions": total_transactions,
                    "total_deposit": float(total_deposit),
                    "total_withdrawal": float(total_withdrawal),
                    "net_flow": float(total_deposit - total_withdrawal)
                },
                "financial_profile": profile_data
            }
        )
