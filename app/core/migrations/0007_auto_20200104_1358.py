# Generated by Django 3.0.2 on 2020-01-04 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200104_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]