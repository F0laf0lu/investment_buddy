from django.urls import path
from ..views.chatbot import ChatBotView

urlpatterns = [
    path('chatbot/', ChatBotView.as_view(), name="chatbot-query"),
]