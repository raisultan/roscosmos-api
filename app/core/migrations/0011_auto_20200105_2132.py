# Generated by Django 3.0.2 on 2020-01-05 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200105_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parserlaunch',
            old_name='no_launches',
            new_name='no_launches_saved',
        ),
    ]
