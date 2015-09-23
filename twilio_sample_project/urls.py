from django.conf.urls import include, url
from django.contrib import admin

from browser_calls.views import SupportTicketCreate

urlpatterns = [
    # Your URLs go here
    url(r'^$', SupportTicketCreate.as_view(), name='home'),

    # Include the Django admin
    url(r'^admin/', include(admin.site.urls)),
]
