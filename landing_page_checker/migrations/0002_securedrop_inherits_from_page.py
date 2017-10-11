# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_auto_20170913_2144'),
        ('home', '0011_change_description_header'),
        ('wagtailcore', '0040_page_draft_title'),
        ('landing_page_checker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecuredropPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('organization', models.CharField(max_length=255, unique=True, verbose_name='Organization')),
                ('landing_page_domain', models.CharField(max_length=255, unique=True, verbose_name='Landing Page Domain Name')),
                ('onion_address', models.CharField(max_length=255, unique=True, verbose_name='SecureDrop Onion Address')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='directory.DirectoryPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.RemoveField(
            model_name='securedrop',
            name='page',
        ),
        migrations.AlterField(
            model_name='result',
            name='securedrop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='landing_page_checker.SecuredropPage'),
        ),
        migrations.DeleteModel(
            name='Securedrop',
        ),
    ]
