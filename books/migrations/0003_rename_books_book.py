# Generated by Django 3.2.10 on 2022-01-08 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_usermaster_books'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
