# Generated by Django 3.2.10 on 2021-12-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20211230_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumaster',
            name='Mid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='SMid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
