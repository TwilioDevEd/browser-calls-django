from django.forms import ModelForm

from .models import SupportTicket

class SupportTicketForm(ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['name', 'phone_number', 'description']
