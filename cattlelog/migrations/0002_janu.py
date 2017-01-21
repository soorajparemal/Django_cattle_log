# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattlelog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='janu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Janu', max_length=200)),
                ('age', models.IntegerField(default=20)),
                ('location', models.CharField(default='Kerala', max_length=200)),
                ('sex', models.CharField(default='Female', max_length=200)),
                ('arrival', models.CharField(default='January 26th', max_length=200)),
                ('under', models.CharField(default='SangiYojana', max_length=200)),
            ],
        ),
    ]
