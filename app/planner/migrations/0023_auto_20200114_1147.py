# Generated by Django 3.0.2 on 2020-01-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0022_auto_20200114_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtype',
            name='name',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
    ]