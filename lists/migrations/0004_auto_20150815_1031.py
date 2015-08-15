# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20150815_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(to='lists.List'),
        ),
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
