from django.urls import path

from .views import SendEmail

urlpatterns = [
        path('send-email/', SendEmail.as_view(), name='send-email'),
]