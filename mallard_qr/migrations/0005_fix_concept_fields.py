# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from aristotle_mdr.utils.migrations import ConceptMigration

class Migration(ConceptMigration):

    dependencies = [
        ('mallard_qr', '0004_remove_question_response_domain'),
        ('aristotle_mdr', '0013_concept_field_fixer_part1'),
    ]

    models_to_fix = [
        'question',
    ]
