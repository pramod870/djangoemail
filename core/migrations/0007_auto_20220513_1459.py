# Generated by Django 3.2.10 on 2022-05-13 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_customer_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='hier1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.hier1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='hier2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.hier2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='hier3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.hier3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='hier4',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.hier4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='hier5',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.hier5'),
            preserve_default=False,
        ),
    ]
