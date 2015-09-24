from django.conf.urls import url

from .views import support_dashboard, get_token, call

urlpatterns = [
    # URLs for searching for and purchasing a new Twilio number
    url(r'^dashboard$', support_dashboard, name='dashboard'),
    url(r'^token$', get_token, name='token'),
    url(r'^call$', call, name='call'),
]
