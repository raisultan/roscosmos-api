# Generated by Django 3.0.2 on 2020-01-06 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200106_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spacecraft',
            name='launch_vehicles',
            field=models.ManyToManyField(blank=True, to='core.LaunchVehicle'),
        ),
    ]
