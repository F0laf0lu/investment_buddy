from django.urls import path
from ..views.chatbot import ChatBotView, ChatbotPromptView, ChatbotRespondView

urlpatterns = [
    path('chatbot/', ChatBotView.as_view(), name="chatbot-query"),
    path('chatbot/prompts/', ChatbotPromptView.as_view(), name='chatbot-prompt'),
    path('chatbot/respond/', ChatbotRespondView.as_view(), name='chatbot-response')
]