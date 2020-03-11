# Generated by Django 3.0.2 on 2020-01-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0021_auto_20200114_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='slug',
            field=models.SlugField(max_length=16, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='name',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
    ]