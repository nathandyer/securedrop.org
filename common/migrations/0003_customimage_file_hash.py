# Generated by Django 2.0.13 on 2019-02-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20180423_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='customimage',
            name='file_hash',
            field=models.CharField(blank=True, editable=False, max_length=40),
        ),
    ]
