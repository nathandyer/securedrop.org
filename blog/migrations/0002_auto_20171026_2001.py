# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('github', '0001_initial'),
        ('common', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorypage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='release',
            field=models.OneToOneField(blank=True, help_text='Releases can be associated with only one post, which should be a release announcement.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_page', to='github.Release'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage'),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage'),
        ),
    ]
