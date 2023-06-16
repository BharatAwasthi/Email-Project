# email_app/urls.py

from django.urls import path
from .views import  send_mail

urlpatterns = [
    # path('', send_email, name='send_email'),
    path('', send_mail, name="email_sending"),
]
