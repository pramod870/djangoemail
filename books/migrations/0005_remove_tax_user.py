# Generated by Django 3.2.10 on 2022-05-14 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tax',
            name='user',
        ),
    ]
