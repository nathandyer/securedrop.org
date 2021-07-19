# Generated by Django 2.2.24 on 2021-07-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0023_directoryentry_onion_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='directoryentry',
            name='https_preferred',
            field=models.BooleanField(default=False, help_text='Check this box if the onion_address URL should preferrably be shown with https://', verbose_name='HTTPS Preferred?'),
        ),
    ]
