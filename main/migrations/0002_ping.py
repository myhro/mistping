# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('success', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(to='main.Host')),
            ],
        ),
    ]
