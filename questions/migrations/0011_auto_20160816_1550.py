# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20150714_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='my_answer_importance',
            field=models.CharField(max_length=50, choices=[('Mandatory', 'Mandatory'), ('Very Important', 'Very Important'), ('Somewhat Important', 'Somewhat Important'), ('Not Important', 'Not Important')]),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='their_importance',
            field=models.CharField(max_length=50, choices=[('Mandatory', 'Mandatory'), ('Very Important', 'Very Important'), ('Somewhat Important', 'Somewhat Important'), ('Not Important', 'Not Important')]),
        ),
    ]
