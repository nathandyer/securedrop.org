# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-21 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20180308_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directorysettings',
            name='compare_onion_address_text',
        ),
        migrations.RemoveField(
            model_name='directorysettings',
            name='landing_page_link_text',
        ),
        migrations.RemoveField(
            model_name='directorysettings',
            name='security_warning',
        ),
    ]
