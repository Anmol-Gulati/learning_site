# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_quiz_times_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(max_length=1, default='i', choices=[('i', 'In Progress'), ('r', 'In Review'), ('p', 'Published')]),
        ),
    ]
