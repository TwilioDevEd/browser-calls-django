from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import SupportTicketForm
from .models import SupportTicket


class SupportTicketCreate(SuccessMessageMixin, CreateView):
    """Renders the home page and the support ticket form"""
    model = SupportTicket
    fields = ['name', 'phone_number', 'description']
    template_name = 'index.html'
    success_url = reverse_lazy('home')
    success_message = "Your ticket was submitted! An agent will call you soon."
