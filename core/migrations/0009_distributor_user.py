# Generated by Django 3.2.10 on 2022-05-13 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_distributor_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.usermaster'),
            preserve_default=False,
        ),
    ]