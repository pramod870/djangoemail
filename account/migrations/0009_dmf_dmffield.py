# Generated by Django 3.2.10 on 2022-05-05 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_submenu_pagelink'),
    ]

    operations = [
        migrations.CreateModel(
            name='DMFField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DMF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=500)),
                ('fields', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.dmffield')),
            ],
        ),
    ]
