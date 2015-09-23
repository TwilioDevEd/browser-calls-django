from django.contrib import admin

from .models import SupportTicket


class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')

admin.site.register(SupportTicket, SupportTicketAdmin)
