from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from browser_calls.views import SupportTicketCreate

urlpatterns = [
    # Your URLs go here
    url(r'^$', SupportTicketCreate.as_view(), name='home'),
    url(r'^support/', include('browser_calls.urls')),

    # Include the Django admin
    url(r'^admin/', include(admin.site.urls)),
]
