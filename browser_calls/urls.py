from django.conf.urls import url

from .views import support_dashboard

urlpatterns = [
    # URLs for searching for and purchasing a new Twilio number
    url(r'^/dashboard$', support_dashboard, name='support_dashboard'),
]
