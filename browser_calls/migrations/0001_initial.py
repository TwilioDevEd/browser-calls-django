# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='SupportTicket',
            fields=[
                (
                    'id',
                    models.AutoField(
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100)),
                (
                    'phone_number',
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128
                    ),
                ),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        )
    ]
