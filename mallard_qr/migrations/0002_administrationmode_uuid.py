# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mallard_qr', '0001_squashed_0005_fix_concept_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrationmode',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid1, help_text='Universally-unique Identifier. Uses UUID1 as this improves uniqueness and tracking between registries', unique=True, editable=False),
        ),
    ]
