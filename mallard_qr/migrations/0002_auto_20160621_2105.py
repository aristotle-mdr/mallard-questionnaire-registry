# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallard_qr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsedomain',
            name='order',
            field=models.PositiveSmallIntegerField(help_text='If a dataset is ordered, this indicates which position this item is in a dataset.', null=True, verbose_name='Position', blank=True),
        ),
        migrations.AlterField(
            model_name='responsedomain',
            name='question',
            field=models.ForeignKey(related_name='response_domains', to='mallard_qr.Question'),
        ),
    ]
