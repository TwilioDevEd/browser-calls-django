from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from twilio import twiml
from twilio.util import TwilioCapability

from .forms import SupportTicketForm
from .models import SupportTicket


class SupportTicketCreate(SuccessMessageMixin, CreateView):
    """Renders the home page and the support ticket form"""
    model = SupportTicket
    fields = ['name', 'phone_number', 'description']
    template_name = 'index.html'
    success_url = reverse_lazy('home')
    success_message = "Your ticket was submitted! An agent will call you soon."

def support_dashboard(request):
    """Shows the list of support tickets to a support agent"""
    context = {}

    context['support_tickets'] = SupportTicket.objects.order_by('-timestamp')

    capability = TwilioCapability(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN)

    capability.allow_client_outgoing(settings.TWIML_APPLICATION_SID)
    context['token'] = capability.generate()

    return render(request, 'browser_calls/support_dashboard.html', context)

@csrf_exempt
def call(request):
    """Returns TwiML instructions to Twilio's POST requests"""
    response = twiml.Response()

    with response.dial(callerId=settings.TWILIO_NUMBER) as r:
        r.number(request.POST['phoneNumber'])

    return HttpResponse(str(response))
