# Generated by Django 3.2.10 on 2021-12-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_menumaster_submenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumaster',
            name='IconImage',
            field=models.ImageField(null=True, upload_to='MenuImages'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='IconImage',
            field=models.ImageField(null=True, upload_to='SubMenuImages'),
        ),
    ]
