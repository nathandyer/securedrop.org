# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-23 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('teaser_title', models.CharField(max_length=60)),
                ('teaser_description', models.CharField(help_text='A one sentence description displayed with the feature overview.', max_length=255)),
                ('description', wagtail.fields.RichTextField(blank=True, null=True)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='MarketingIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('subtitle', models.CharField(blank=True, help_text='Appears immediately below page title.', max_length=255, null=True)),
                ('body', wagtail.fields.StreamField((('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')]))))), ('raw_html', wagtail.blocks.RawHTMLBlock()), ('blockquote', wagtail.blocks.StructBlock((('text', wagtail.blocks.RichTextBlock()), ('source_text', wagtail.blocks.RichTextBlock(required=False)), ('source_url', wagtail.blocks.URLBlock(help_text='Source text will link to this url.', required=False))))), ('list', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='List Item'), template='common/blocks/list_block_columns.html')), ('video', wagtail.blocks.StructBlock((('video', wagtail.embeds.blocks.EmbedBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')]))))), ('heading_1', wagtail.blocks.StructBlock((('content', wagtail.blocks.CharBlock()),))), ('heading_2', wagtail.blocks.StructBlock((('content', wagtail.blocks.CharBlock()),))), ('heading_3', wagtail.blocks.StructBlock((('content', wagtail.blocks.CharBlock()),)))), blank=True, null=True)),
                ('subheader', models.CharField(default='How to install SecureDrop at your organization.', help_text='Displayed below features.', max_length=255)),
                ('how_to_install_subtitle', models.CharField(blank=True, help_text='Appears immediately below subheader.', max_length=255, null=True)),
                ('how_to_install_body', wagtail.fields.StreamField((('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')]))))), ('raw_html', wagtail.blocks.RawHTMLBlock()), ('blockquote', wagtail.blocks.StructBlock((('text', wagtail.blocks.RichTextBlock()), ('source_text', wagtail.blocks.RichTextBlock(required=False)), ('source_url', wagtail.blocks.URLBlock(help_text='Source text will link to this url.', required=False))))), ('list', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='List Item'), template='common/blocks/list_block_columns.html')), ('video', wagtail.blocks.StructBlock((('video', wagtail.embeds.blocks.EmbedBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')]))))), ('heading_1', wagtail.blocks.StructBlock((('content', wagtail.blocks.CharBlock()),))), ('heading_2', wagtail.blocks.StructBlock((('content', wagtail.blocks.CharBlock()),))), ('heading_3', wagtail.blocks.StructBlock((('content', wagtail.blocks.CharBlock()),)))), blank=True, null=True)),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='OrderedFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marketing_orders', to='marketing.FeaturePage')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='marketing.MarketingIndexPage')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='orderedfeatures',
            unique_together=set([('page', 'feature')]),
        ),
    ]
