from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from browser_calls.views import SupportTicketCreate

urlpatterns = [
    # Your URLs go here
    path('', SupportTicketCreate.as_view(), name='home'),
    path('support/', include('browser_calls.urls')),

    # Include the Django admin
    path('admin/', admin.site.urls),
]
