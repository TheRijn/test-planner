# Generated by Django 3.0.2 on 2020-01-14 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0018_auto_20200114_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availibility',
            old_name='extras',
            new_name='_extras',
        ),
        migrations.RenameField(
            model_name='availibility',
            old_name='host',
            new_name='_host',
        ),
        migrations.RenameField(
            model_name='availibility',
            old_name='location',
            new_name='_location',
        ),
        migrations.RenameField(
            model_name='availibility',
            old_name='slot_length',
            new_name='_slot_length',
        ),
        migrations.RenameField(
            model_name='eventtype',
            old_name='extras',
            new_name='_extras',
        ),
        migrations.RenameField(
            model_name='eventtype',
            old_name='host',
            new_name='_host',
        ),
        migrations.RenameField(
            model_name='eventtype',
            old_name='location',
            new_name='_location',
        ),
        migrations.RenameField(
            model_name='eventtype',
            old_name='slot_length',
            new_name='_slot_length',
        ),
    ]
