# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_sample_data(apps, schema_editor):
    """Prepopulate the app with some sample data"""
    SupportTicket = apps.get_model('browser_calls', 'SupportTicket')

    SupportTicket.objects.create(
        name='Charles Holdsworth',
        phone_number='+14153674129',
        description="I played for Middlesex in the championships and my \
        mallet squeaked the whole time! I demand a refund!")

    SupportTicket.objects.create(
        name='John Woodger',
        phone_number='+15712812415',
        description='The mallet you sold me broke! Call me immediately!')


class Migration(migrations.Migration):

    dependencies = [
        ('browser_calls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_data),
    ]
