# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-19 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0054_add_banned_email_ids_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengephasesplit',
            name='is_leaderboard_order_descending',
            field=models.BooleanField(default=True),
        ),
    ]
