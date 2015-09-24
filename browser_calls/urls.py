from django.conf.urls import url

from .views import support_dashboard, call

urlpatterns = [
    # URLs for searching for and purchasing a new Twilio number
    url(r'^dashboard$', support_dashboard, name='support_dashboard'),
    url(r'^call$', call, name='call'),
]
