from django.urls import path

from .views import support_dashboard, get_token, call

urlpatterns = [
    # URLs for searching for and purchasing a new Twilio number
    path('dashboard', support_dashboard, name='dashboard'),
    path('token', get_token, name='token'),
    path('call', call, name='call'),
]
