from django.urls import path
from ..views.investment_portfolio import (InvestmentPortfolioCreateView, InvestmentPortfolioDetailView,
                                          InvestmentPortfolioListView, InvestmentPortfolioUpdateView)

urlpatterns = [
    path('portfolio/', InvestmentPortfolioCreateView.as_view(), name='portfolio-create'),
    path('portfolio/all/', InvestmentPortfolioListView.as_view(), name='portfolio-user-list'),
    path('portfolio/detail/<uuid:id>', InvestmentPortfolioDetailView.as_view(), name='portfolio-detail'),
    path('portfolio/update/<uuid:id>', InvestmentPortfolioUpdateView.as_view(), name='portfolio-update'),
]