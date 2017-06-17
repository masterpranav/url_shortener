# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-13 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20170613_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]