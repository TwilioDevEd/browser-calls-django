from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class SupportTicket(models.Model):
    """A support ticket submitted by an unsatisfied customer :("""

    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(
        help_text='Must include international prefix - e.g. +1 555 555 55555')
    description = models.TextField(help_text='A description of your problem')

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '#{0} - {1}'.format(self.id, self.name)
