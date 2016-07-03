# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_mdr', '0012_better_workflows'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrationMode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.TextField(help_text='The primary name used for human identification purposes.')),
                ('definition', ckeditor_uploader.fields.RichTextUploadingField(help_text='Representation of a concept by a descriptive statement which serves to differentiate it from related concepts', verbose_name='definition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('_concept_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aristotle_mdr._concept')),
                ('short_name', models.CharField(max_length=100, blank=True)),
                ('version', models.CharField(max_length=20, blank=True)),
                ('synonyms', models.CharField(max_length=200, blank=True)),
                ('references', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('origin_URI', models.URLField(help_text='If imported, the original location of the item', blank=True)),
                ('comments', ckeditor_uploader.fields.RichTextUploadingField(help_text='Descriptive comments about the metadata item.', blank=True)),
                ('submitting_organisation', models.CharField(max_length=256, blank=True)),
                ('responsible_organisation', models.CharField(max_length=256, blank=True)),
                ('question_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('instruction_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('estimated_seconds_response_time', models.PositiveIntegerField(help_text='he estimated amount of time required to answer a question expressed in seconds.', null=True, blank=True)),
                ('collected_data_element', models.ForeignKey(related_name='questions', blank=True, to='aristotle_mdr.DataElement', null=True)),
                ('response_domain', models.ManyToManyField(to='aristotle_mdr.ValueDomain', null=True, verbose_name='Value Domain', blank=True)),
                ('superseded_by', models.ForeignKey(related_name='supersedes', blank=True, to='mallard_qr.Question', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('aristotle_mdr._concept',),
        ),
        migrations.CreateModel(
            name='ResponseDomain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('maximum_occurances', models.PositiveIntegerField(default=1, help_text='The maximum number of times a response can be included in a question')),
                ('minimum_occurances', models.PositiveIntegerField(default=1, help_text='The minimum number of times a response can be included in a question')),
                ('blank_is_missing_value', models.BooleanField(default=False, help_text='When value is true a blank or empty variable content should be treated as a missing value.')),
                ('question', models.ForeignKey(to='mallard_qr.Question')),
                ('value_domain', models.ForeignKey(to='aristotle_mdr.ValueDomain')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
