# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallard_qr', '0002_auto_20160621_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='responsedomain',
            options={'ordering': ['order']},
        ),
    ]
