# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-20 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jetty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=255, verbose_name='app_label')),
                ('model', models.CharField(max_length=255, verbose_name='model')),
                ('layout', models.TextField(blank='', default='', verbose_name='layout')),
                ('date_add', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added')),
            ],
            options={
                'verbose_name': 'view settings',
                'verbose_name_plural': 'views settings',
            },
        ),
    ]