from django.db import models

# Create your models here.
class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)


from django.conf import settings
from django.db.models import ForeignKey, CASCADE, Model
from gst_field.modelfields import GSTField, PANField

class Tax(models.Model):
    # user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    gstin = GSTField()
    pan = PANField()




class Sales(models.Model):
    Bill_Date = models.DateField()
    Invoice_No = models.CharField(max_length=50)
    Tally_MasterID = models.CharField(max_length=15, null=True, blank=True)
    Total_Inventory_Amount = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
    Total_GST = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
    SGST_AMOUNT = models.DecimalField(max_digits=20,decimal_places=2 , null=True, blank=True)
    CGST_AMOUNT = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
    IGST_AMOUNT = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
    Cash_Discount_Amount = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
    R_O_Amount = models.DecimalField(max_digits=20,decimal_places=2,null=True, blank=True )
    Total_Invoice_Amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.items

    # @property
    # def full_name(self):
    #     "Returns the person's full name."
    #     return '%s %s' % (self.first_name, self.last_name)


    def save(self, *args, **kwargs):
        self.Total_Invoice_Amount = self.CGST_AMOUNT + self.SGST_AMOUNT
        super(Sales, self).save(*args, **kwargs)


class Sales_Detail(models.Model):
    Sales_Item_Name = models.CharField(max_length=50 ,null=True, blank=True)
    Sales_Quantity = models.PositiveIntegerField()
    Sales_Rate = models.DecimalField(max_digits=20, decimal_places=2)
    Sales_Serial_No = models.CharField(max_length=50)
    Sales_Batch = models.CharField(max_length=50)
    Sales_Discount = models.PositiveIntegerField(null=True)
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2,default=0)
    Reference_No = models.CharField(max_length=50, null=True, blank=True)
    SalesDetails = models.ForeignKey(Sales, on_delete=models.CASCADE, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sales Detail"
    #
    #
    # @property
    # def Total_Amount(self):
    #     return self.Sales_Quantity*self.Sales_Rate
    #
    #


    def __str__(self):
        res = self.Sales_Quantity
        return str(res)











class Opening_Balance(models.Model):
    Distributor_Name = models.CharField(max_length=50)
    Date = models.DateTimeField()
    Opening_Stock_Details = models.ForeignKey(Sales_Detail, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Opening Balance"

    def __unicode__(self):
        return self.Distributor_Code

    def __str__(self):
        return self.Distributor_Code




class SalesReturn(models.Model):
    Bill_Date = models.DateTimeField()
    Invoice_No = models.CharField(max_length=20)
    Tally_Master_ID = models.CharField(max_length=15)
    Total_Inventory_Amount = models.FloatField(null=True)
    Total_GST = models.FloatField(null=True)
    SGST_AMOUNT = models.FloatField(null=True)
    CGST_AMOUNT = models.FloatField(null=True)
    IGST_AMOUNT = models.FloatField(null=True)
    Cash_Discount_Amount = models.FloatField(null=True)
    RO_Amount = models.FloatField(null=True)
    Details_Of_Sales_Return = models.ForeignKey(Sales_Detail,on_delete=models.CASCADE)
    Total_Invoice_Amount = models.CharField(max_length=20, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sales Return"



    @property
    def total_price(self):
        cost = 0
        for item in self.items.all():
            cost += item.total_price
        return str(cost)




class DetailOfPurchase(models.Model):
    item_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Item Name')
    Purchases_Quantity = models.PositiveIntegerField(verbose_name='Purchase Quantity')
    Purchase_Rate = models.FloatField(verbose_name='Purchase Rate')
    Purchase_Product_Discount = models.FloatField(null=True, blank=True, default=0, verbose_name='Purchase Product Discount')
    Purchases_Serial_No = models.CharField(max_length=50, verbose_name='Puchase Serial No')
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Total Amount')
    Total_Amounts = models.CharField(max_length=50, null=True, blank=True, verbose_name='Total Amounts')

    class Meta:
        verbose_name = "Purchase Document Detail"

    def __str__(self):
        return self.item_name


class PurchaseDocument(models.Model):
    vendor_choice = (
        ('Johnson and Johnson Surgical Vision India Pvt. Ltd.','Johnson and Johnson Surgical Vision India Pvt. Ltd.'),
        ('Johnson and Johnson .', 'Johnson and Johnson '),
    )
    # distributor_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Distributor Name')
    Bill_Date = models.DateField(verbose_name='Bill Date')
    Supplier_Invoice_No = models.CharField(max_length=50, verbose_name='Supplier Invoice No')
    SAP_Order_No = models.CharField(max_length=50, null=True, blank=True, verbose_name='SAP Order No')
    SAP_Order_Date = models.DateField(verbose_name='SAP Order Date')
    Total_Inventory_Amount = models.FloatField(null=True, verbose_name='Total Inventory Amount')
    Total_GST = models.FloatField(null=True, verbose_name='Total GST')
    SGST_AMOUNT = models.FloatField(null=True, verbose_name='SGST AMOUNT')
    CGST_AMOUNT = models.FloatField(null=True, verbose_name='CGST AMOUNT')
    IGST_AMOUNT = models.FloatField(null=True, verbose_name='IGST AMOUNT')
    Details_Of_Purchase = models.ForeignKey(DetailOfPurchase, on_delete=models.CASCADE,verbose_name= 'Details Of Purchase')
    Vendor_Name = models.CharField(max_length=100, choices=vendor_choice, verbose_name='Vendor Name')
    PO_No = models.CharField(max_length=50, null=True, blank=True, verbose_name='PO No')
    Total_Invoice_Amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total Invoice Amount')

    class Meta:
        verbose_name = "Purchase Document"



    def __int__(self):
        return self.Total_Invoice_Amount


class DetailsOfPurchaseReturn(models.Model):
    Purchases_Return_Quantity = models.PositiveIntegerField(verbose_name='Purchase Return Quantity')
    Purchase_Rate = models.FloatField(verbose_name='Purchase Rate')
    Purchase_Product_Discount = models.FloatField(null=True, blank=True, default=0, verbose_name='Purchase Product Discount')
    Purchases_Serial_No = models.CharField(max_length=50, verbose_name='Puchase Serial No')
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Total Amount')
    Total_Amounts = models.CharField(max_length=50, null=True, blank=True, verbose_name='Total Amounts')

    class Meta:
        verbose_name = "Purchase Return Detail"

    def __str__(self):
        res= self.items
        return str(res)







class PurchaseReturnDocument(models.Model):
    vendor_choice = (
        ('Johnson and Johnson Surgical Vision India Pvt. Ltd.','Johnson and Johnson Surgical Vision India Pvt. Ltd.'),
        ('Johnson and Johnson .', 'Johnson and Johnson '),
    )
    Bill_Date = models.DateField(verbose_name='Bill Date')
    Supplier_Invoice_No = models.CharField(max_length=50, verbose_name='Supplier Invoice No')
    SAP_Order_No = models.CharField(max_length=50,null=True,blank=True, verbose_name='SAP Order No')
    SAP_Order_Date = models.DateField(verbose_name='SAP Order Date')
    Total_Inventory_Amount = models.FloatField(null=True, verbose_name='Total Inventory Amount')
    Total_GST = models.FloatField(null=True, verbose_name='Total GST')
    SGST_AMOUNT = models.FloatField(null=True, verbose_name='SGST AMOUNT')
    CGST_AMOUNT = models.FloatField(null=True, verbose_name='CGST AMOUNT')
    IGST_AMOUNT = models.FloatField(null=True, verbose_name='IGST AMOUNT')
    Details_Of_Purchase_Return = models.ForeignKey(DetailsOfPurchaseReturn, on_delete=models.CASCADE,verbose_name='Details Of Purchase Return', null=True, blank=True)
    Vendor_Name = models.CharField(max_length=100, choices=vendor_choice, verbose_name='Vendor Name')
    PO_No = models.CharField(max_length=50, null=True, blank=True, verbose_name='PO No')
    Total_Invoice_Amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Total Invoice Amount')

    class Meta:
        verbose_name = "Purchase Return Document Detail"

    def __str__(self):
        return self.Vendor_Name





class Delivery_Note(models.Model):
    # Customer_Name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Customer Name')
    Bill_Date = models.DateField(verbose_name='Bill Date')
    Invoice_No = models.CharField(max_length=100, verbose_name='Invoice No')
    Total_Inventory_Amount = models.CharField(max_length=100, verbose_name='Total Inventory Amount')
    Total_GST = models.DecimalField(max_digits=20, decimal_places=2,default=0, verbose_name='Total GST',null=True, blank=True)
    SGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='SGST AMOUNT',null=True, blank=True)
    CGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='CGST AMOUNT',null=True, blank=True)
    IGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='IGST AMOUNT',null=True, blank=True)
    Cash_Discount_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='Cash Discount Amount', null=True, blank=True)
    R_O_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='R O AMOUNT', null=True, blank=True)
    Total_Amount = models.CharField(max_length=20,verbose_name="Total Amount")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Delivery Note"
    def __str__(self):
        return self.Invoice_No





class Delivery_Note_Details(models.Model):
    Deliverynotes = models.ForeignKey(Delivery_Note, on_delete=models.CASCADE , null=True, blank=True)
    Quantity = models.PositiveIntegerField(verbose_name='Sales Quantity*')
    Rate = models.FloatField(verbose_name='Sales Rate')
    Serial_No = models.CharField(max_length=50, verbose_name='Sales Serial No*')
    Batch = models.CharField(max_length=50, verbose_name="Sales Batch", null=True, blank=True)
    Discount = models.FloatField(null=True, blank=True, default=0, verbose_name='Sales Discount')
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='*Total Amount')
    Reference_No = models.CharField(max_length=50, verbose_name='Reference No', null=True,blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Delivery Note Detail"


    def __str__(self):
        return self.Serial_No



class Receipt_Note(models.Model):
    Bill_Date = models.DateField(verbose_name='Bill Date')
    Invoice_No = models.CharField(max_length=100, verbose_name='Invoice No')
    Total_Inventory_Amount = models.CharField(max_length=100, verbose_name='Total Inventory Amount')
    Total_GST = models.DecimalField(max_digits=20, decimal_places=2,default=0, verbose_name='Total GST',null=True, blank=True)
    SGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='SGST AMOUNT',null=True, blank=True)
    CGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='CGST AMOUNT',null=True, blank=True)
    IGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='IGST AMOUNT',null=True, blank=True)
    Cash_Discount_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='Cash Discount Amount', null=True, blank=True)
    R_O_Amount = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='R O AMOUNT', null=True, blank=True)
    Total_Amount = models.CharField(max_length=20,verbose_name="Total Amount")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Receipt Note"

    def __str__(self):
        return str(self.Total_Amount)





class Receipt_Note_Detail(models.Model):
    receiptnotes = models.ForeignKey(Receipt_Note, on_delete=models.CASCADE , null=True, blank=True, verbose_name='Receipt Note')
    Quantity = models.PositiveIntegerField(verbose_name='Sales Quantity*')
    Rate = models.FloatField(verbose_name='Sales Rate')
    Serial_No = models.CharField(max_length=50, verbose_name='Sales Serial No*')
    Batch = models.CharField(max_length=50, verbose_name="Sales Batch", null=True, blank=True)
    Discount = models.FloatField(null=True, blank=True, default=0, verbose_name='Sales Discount')
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='*Total Amount')
    Reference_No = models.CharField(max_length=50, verbose_name='Reference No', null=True,blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Receipt Note Detail"




    def save(self, *args, **kwargs):
        self.Total_Amount = self.Rate * self.Quantity - self.Discount
        super(Receipt_Note_Detail, self).save(*args, **kwargs)





class DocumentMasterType(models.Model):
    choice_field = (
       ('Sales','Sales'),
       ('SalesReturn','SalesReturn'),
    )
    sales = models.ForeignKey(Sales, on_delete=models.SET_NULL, null=True,blank=True)
    salesreturn = models.ForeignKey(SalesReturn, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.Invoice_No



