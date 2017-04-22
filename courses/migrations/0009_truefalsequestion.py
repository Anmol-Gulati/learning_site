# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_multiplechoicequestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrueFalseQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='courses.Question', primary_key=True)),
            ],
            bases=('courses.question',),
        ),
    ]
