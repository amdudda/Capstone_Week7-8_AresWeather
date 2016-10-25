# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terrestrial_date', models.DateField()),
                ('sol', models.IntegerField()),
                ('ls', models.FloatField()),
                ('min_temp', models.FloatField(verbose_name='low temp in Centigrade')),
                ('min_temp_fahrenheit', models.FloatField(verbose_name='low temp in Fahrenheit')),
                ('max_temp', models.FloatField(verbose_name='high temp in Centigrade')),
                ('max_temp_fahrenheit', models.FloatField(verbose_name='high temp in Fahrenheit')),
                ('pressure', models.FloatField()),
                ('pressure_string', models.CharField(max_length=100, verbose_name='pressure descriptor')),
                ('abs_humidity', models.FloatField(verbose_name='absolute humidity')),
                ('wind_speed', models.FloatField()),
                ('atmo_opacity', models.CharField(max_length=100, verbose_name='atmospheric conditions')),
                ('season', models.CharField(max_length=10)),
                ('sunrise', models.DateTimeField()),
                ('sunset', models.DateTimeField()),
            ],
        ),
    ]