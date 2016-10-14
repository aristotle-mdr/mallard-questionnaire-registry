# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallard_qr', '0003_auto_20160703_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='response_domain',
        ),
    ]
