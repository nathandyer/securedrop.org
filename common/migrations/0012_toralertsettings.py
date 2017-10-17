# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('common', '0011_add_metadata_mixin'),
    ]

    operations = [
        migrations.CreateModel(
            name='TorAlertSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Have a document to share?', help_text='Displayed if user is not browsing with Tor.', max_length=255)),
                ('subtitle', models.CharField(blank=True, default='Your security is compromised while using this browser.', max_length=255, null=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Text explaining how and why to use Tor browser. Only displayed if user is not browsing with Tor.', null=True)),
                ('tor_settings_title', models.CharField(default='Your Tor security settings are too low. Only displayed if user is browsing with Tor already.', max_length=255)),
                ('tor_settings_subtitle', models.CharField(blank=True, default='These settings allow JavaScript to run which compromises your security.', max_length=255, null=True)),
                ('tor_settings_body', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Text explaining how and why to change Tor security settings.', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
