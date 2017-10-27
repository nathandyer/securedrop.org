# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('common', '0001_initial'),
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('source_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('source_url', wagtail.wagtailcore.blocks.URLBlock(help_text='Source text will link to this url.', required=False))))), ('list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='List Item'), template='common/blocks/list_block_columns.html')), ('video', wagtail.wagtailcore.blocks.StructBlock((('video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))))), ('heading_1', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),))), ('heading_2', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),))), ('heading_3', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),)))), blank=True, null=True)),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage')),
                ('sidebar_menu', models.ForeignKey(blank=True, help_text="If left empty, page will use parent's sidebar menu", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='menus.Menu')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='FaqQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('question', models.CharField(max_length=255)),
                ('answer', wagtail.wagtailcore.fields.RichTextField()),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='simple.FAQPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('source_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('source_url', wagtail.wagtailcore.blocks.URLBlock(help_text='Source text will link to this url.', required=False))))), ('list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='List Item'), template='common/blocks/list_block_columns.html')), ('video', wagtail.wagtailcore.blocks.StructBlock((('video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))))), ('heading_1', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),))), ('heading_2', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),))), ('heading_3', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),)))))),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='SimplePageWithMenuSidebar',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('source_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('source_url', wagtail.wagtailcore.blocks.URLBlock(help_text='Source text will link to this url.', required=False))))), ('list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='List Item'), template='common/blocks/list_block_columns.html')), ('video', wagtail.wagtailcore.blocks.StructBlock((('video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('full-width', 'Full Width')]))))), ('heading_1', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),))), ('heading_2', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),))), ('heading_3', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock()),)))))),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage')),
                ('sidebar_menu', models.ForeignKey(blank=True, help_text="If left empty, page will use parent's sidebar menu", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='menus.Menu')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
    ]
