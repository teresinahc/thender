# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-05 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160305_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100)),
                ('sigla', models.CharField(blank=True, max_length=8)),
            ],
        ),
        migrations.AlterModelOptions(
            name='candidato',
            options={'ordering': ('nome', 'legenda')},
        ),
        migrations.AlterField(
            model_name='candidato',
            name='legenda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Legenda'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='nome',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
