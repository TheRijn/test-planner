# Generated by Django 3.0.2 on 2020-01-29 15:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0029_auto_20200129_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventappointment',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='planner.Event'),
        ),
        migrations.AlterField(
            model_name='eventappointment',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]