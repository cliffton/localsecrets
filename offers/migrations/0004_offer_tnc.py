# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_offer_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='tnc',
            field=models.TextField(null=True),
        ),
    ]
