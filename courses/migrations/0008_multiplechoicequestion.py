# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(serialize=False, parent_link=True, to='courses.Question', primary_key=True, auto_created=True)),
                ('shuffle_answers', models.BooleanField(default=False)),
            ],
            bases=('courses.question',),
        ),
    ]
