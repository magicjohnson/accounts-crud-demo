# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 09:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=512, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=512, verbose_name='Last Name')),
                ('iban', models.CharField(max_length=34, validators=[main.validators.IbanValidator()], verbose_name='IBAN')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
        ),
    ]
