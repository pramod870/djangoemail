# Generated by Django 3.2.10 on 2022-01-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20220103_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='pageLink',
            field=models.CharField(choices=[('Bill Wise Sales Report', 'Bill Wise Sales Report'), ('Bill Wise Sales Report Detailed', 'Bill Wise Sales Report Detailed'), ('Bill Wise Sales Report old', 'Bill Wise Sales Report old'), ('Access Control', 'Access Control'), ('Asign Users', 'Asign Users'), ('Consolidated Sync Report Admin', 'Consolidated Sync Report Admin'), ('Dashboad Config', 'Dashboad Config'), ('Distributor MIS Report', 'Distributor MIS Report'), ('Document Upload', 'Document Uploader'), ('Dynamic Forms', 'Dynamic Forms'), ('Dynamic Work Flow', 'Dynamic Work Flow'), ('Error', 'Error'), ('Explorer', 'Explorer'), ('FTP', 'FTP'), ('Holiday', 'Holiday'), ('Invoice Explorer', 'Invoice Explorer'), ('Kill Request', 'Kill Request'), ('LastTransactionReportLog', 'LastTransactionReportLog'), ('Location', 'Location'), ('Manage Account', 'Manage Account'), ('Master Map Settings', 'Master Map Settings'), ('Menu Control', 'Menu Control')], max_length=50),
        ),
    ]
