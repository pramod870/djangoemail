# Generated by Django 3.2.10 on 2022-06-09 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_tax_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bill_Date', models.DateField(verbose_name='Bill Date')),
                ('Invoice_No', models.CharField(max_length=100, verbose_name='Invoice No')),
                ('Total_Inventory_Amount', models.CharField(max_length=100, verbose_name='Total Inventory Amount')),
                ('Total_GST', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='Total GST')),
                ('SGST_AMOUNT', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='SGST AMOUNT')),
                ('CGST_AMOUNT', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='CGST AMOUNT')),
                ('IGST_AMOUNT', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='IGST AMOUNT')),
                ('Cash_Discount_Amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='Cash Discount Amount')),
                ('R_O_Amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='R O AMOUNT')),
                ('Total_Amount', models.CharField(max_length=20, verbose_name='Total Amount')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Delivery Note',
            },
        ),
        migrations.CreateModel(
            name='DetailOfPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Item Name')),
                ('Purchases_Quantity', models.PositiveIntegerField(verbose_name='Purchase Quantity')),
                ('Purchase_Rate', models.FloatField(verbose_name='Purchase Rate')),
                ('Purchase_Product_Discount', models.FloatField(blank=True, default=0, null=True, verbose_name='Purchase Product Discount')),
                ('Purchases_Serial_No', models.CharField(max_length=50, verbose_name='Puchase Serial No')),
                ('Total_Amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Total Amount')),
                ('Total_Amounts', models.CharField(blank=True, max_length=50, null=True, verbose_name='Total Amounts')),
            ],
            options={
                'verbose_name': 'Purchase Document Detail',
            },
        ),
        migrations.CreateModel(
            name='DetailsOfPurchaseReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Purchases_Return_Quantity', models.PositiveIntegerField(verbose_name='Purchase Return Quantity')),
                ('Purchase_Rate', models.FloatField(verbose_name='Purchase Rate')),
                ('Purchase_Product_Discount', models.FloatField(blank=True, default=0, null=True, verbose_name='Purchase Product Discount')),
                ('Purchases_Serial_No', models.CharField(max_length=50, verbose_name='Puchase Serial No')),
                ('Total_Amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Total Amount')),
                ('Total_Amounts', models.CharField(blank=True, max_length=50, null=True, verbose_name='Total Amounts')),
            ],
            options={
                'verbose_name': 'Purchase Return Detail',
            },
        ),
        migrations.CreateModel(
            name='Receipt_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bill_Date', models.DateField(verbose_name='Bill Date')),
                ('Invoice_No', models.CharField(max_length=100, verbose_name='Invoice No')),
                ('Total_Inventory_Amount', models.CharField(max_length=100, verbose_name='Total Inventory Amount')),
                ('Total_GST', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='Total GST')),
                ('SGST_AMOUNT', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='SGST AMOUNT')),
                ('CGST_AMOUNT', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='CGST AMOUNT')),
                ('IGST_AMOUNT', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='IGST AMOUNT')),
                ('Cash_Discount_Amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='Cash Discount Amount')),
                ('R_O_Amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='R O AMOUNT')),
                ('Total_Amount', models.CharField(max_length=20, verbose_name='Total Amount')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Receipt Note',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bill_Date', models.DateField()),
                ('Invoice_No', models.CharField(max_length=50)),
                ('Tally_MasterID', models.CharField(blank=True, max_length=15, null=True)),
                ('Total_Inventory_Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Total_GST', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('SGST_AMOUNT', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('CGST_AMOUNT', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('IGST_AMOUNT', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Cash_Discount_Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('R_O_Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Total_Invoice_Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sales_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sales_Item_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Sales_Quantity', models.PositiveIntegerField()),
                ('Sales_Rate', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Sales_Serial_No', models.CharField(max_length=50)),
                ('Sales_Batch', models.CharField(max_length=50)),
                ('Sales_Discount', models.PositiveIntegerField(null=True)),
                ('Total_Amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('Reference_No', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('SalesDetails', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.sales')),
            ],
            options={
                'verbose_name': 'Sales Detail',
            },
        ),
        migrations.CreateModel(
            name='SalesReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bill_Date', models.DateTimeField()),
                ('Invoice_No', models.CharField(max_length=20)),
                ('Tally_Master_ID', models.CharField(max_length=15)),
                ('Total_Inventory_Amount', models.FloatField(null=True)),
                ('Total_GST', models.FloatField(null=True)),
                ('SGST_AMOUNT', models.FloatField(null=True)),
                ('CGST_AMOUNT', models.FloatField(null=True)),
                ('IGST_AMOUNT', models.FloatField(null=True)),
                ('Cash_Discount_Amount', models.FloatField(null=True)),
                ('RO_Amount', models.FloatField(null=True)),
                ('Total_Invoice_Amount', models.CharField(max_length=20, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('Details_Of_Sales_Return', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.sales_detail')),
            ],
            options={
                'verbose_name': 'Sales Return',
            },
        ),
        migrations.CreateModel(
            name='Receipt_Note_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField(verbose_name='Sales Quantity*')),
                ('Rate', models.FloatField(verbose_name='Sales Rate')),
                ('Serial_No', models.CharField(max_length=50, verbose_name='Sales Serial No*')),
                ('Batch', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sales Batch')),
                ('Discount', models.FloatField(blank=True, default=0, null=True, verbose_name='Sales Discount')),
                ('Total_Amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='*Total Amount')),
                ('Reference_No', models.CharField(blank=True, max_length=50, null=True, verbose_name='Reference No')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('receiptnotes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.receipt_note', verbose_name='Receipt Note')),
            ],
            options={
                'verbose_name': 'Receipt Note Detail',
            },
        ),
        migrations.CreateModel(
            name='PurchaseReturnDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bill_Date', models.DateField(verbose_name='Bill Date')),
                ('Supplier_Invoice_No', models.CharField(max_length=50, verbose_name='Supplier Invoice No')),
                ('SAP_Order_No', models.CharField(blank=True, max_length=50, null=True, verbose_name='SAP Order No')),
                ('SAP_Order_Date', models.DateField(verbose_name='SAP Order Date')),
                ('Total_Inventory_Amount', models.FloatField(null=True, verbose_name='Total Inventory Amount')),
                ('Total_GST', models.FloatField(null=True, verbose_name='Total GST')),
                ('SGST_AMOUNT', models.FloatField(null=True, verbose_name='SGST AMOUNT')),
                ('CGST_AMOUNT', models.FloatField(null=True, verbose_name='CGST AMOUNT')),
                ('IGST_AMOUNT', models.FloatField(null=True, verbose_name='IGST AMOUNT')),
                ('Vendor_Name', models.CharField(choices=[('Johnson and Johnson Surgical Vision India Pvt. Ltd.', 'Johnson and Johnson Surgical Vision India Pvt. Ltd.'), ('Johnson and Johnson .', 'Johnson and Johnson ')], max_length=100, verbose_name='Vendor Name')),
                ('PO_No', models.CharField(blank=True, max_length=50, null=True, verbose_name='PO No')),
                ('Total_Invoice_Amount', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Total Invoice Amount')),
                ('Details_Of_Purchase_Return', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.detailsofpurchasereturn', verbose_name='Details Of Purchase Return')),
            ],
            options={
                'verbose_name': 'Purchase Return Document Detail',
            },
        ),
        migrations.CreateModel(
            name='PurchaseDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bill_Date', models.DateField(verbose_name='Bill Date')),
                ('Supplier_Invoice_No', models.CharField(max_length=50, verbose_name='Supplier Invoice No')),
                ('SAP_Order_No', models.CharField(blank=True, max_length=50, null=True, verbose_name='SAP Order No')),
                ('SAP_Order_Date', models.DateField(verbose_name='SAP Order Date')),
                ('Total_Inventory_Amount', models.FloatField(null=True, verbose_name='Total Inventory Amount')),
                ('Total_GST', models.FloatField(null=True, verbose_name='Total GST')),
                ('SGST_AMOUNT', models.FloatField(null=True, verbose_name='SGST AMOUNT')),
                ('CGST_AMOUNT', models.FloatField(null=True, verbose_name='CGST AMOUNT')),
                ('IGST_AMOUNT', models.FloatField(null=True, verbose_name='IGST AMOUNT')),
                ('Vendor_Name', models.CharField(choices=[('Johnson and Johnson Surgical Vision India Pvt. Ltd.', 'Johnson and Johnson Surgical Vision India Pvt. Ltd.'), ('Johnson and Johnson .', 'Johnson and Johnson ')], max_length=100, verbose_name='Vendor Name')),
                ('PO_No', models.CharField(blank=True, max_length=50, null=True, verbose_name='PO No')),
                ('Total_Invoice_Amount', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Total Invoice Amount')),
                ('Details_Of_Purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.detailofpurchase', verbose_name='Details Of Purchase')),
            ],
            options={
                'verbose_name': 'Purchase Document',
            },
        ),
        migrations.CreateModel(
            name='Opening_Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Distributor_Name', models.CharField(max_length=50)),
                ('Date', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('Opening_Stock_Details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.sales_detail')),
            ],
            options={
                'verbose_name': 'Opening Balance',
            },
        ),
        migrations.CreateModel(
            name='Delivery_Note_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField(verbose_name='Sales Quantity*')),
                ('Rate', models.FloatField(verbose_name='Sales Rate')),
                ('Serial_No', models.CharField(max_length=50, verbose_name='Sales Serial No*')),
                ('Batch', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sales Batch')),
                ('Discount', models.FloatField(blank=True, default=0, null=True, verbose_name='Sales Discount')),
                ('Total_Amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='*Total Amount')),
                ('Reference_No', models.CharField(blank=True, max_length=50, null=True, verbose_name='Reference No')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('Deliverynotes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.delivery_note')),
            ],
            options={
                'verbose_name': 'Delivery Note Detail',
            },
        ),
    ]
