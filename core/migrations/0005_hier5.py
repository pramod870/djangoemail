# Generated by Django 3.2.10 on 2022-05-13 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_hier4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hier5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hier5_name', models.CharField(max_length=20)),
                ('hier2', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='core.hier2')),
                ('hier3', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='core.hier3')),
                ('hier4', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='core.hier4')),
                ('hierarchy1', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='core.hier1')),
            ],
        ),
    ]
