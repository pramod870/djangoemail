# Generated by Django 3.2.10 on 2022-08-17 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_citymaster_region_statemaster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statemaster',
            old_name='Region',
            new_name='region',
        ),
    ]
