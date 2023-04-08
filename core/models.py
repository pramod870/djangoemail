from django.db import models

# Create your models here.

class dummy(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


    def __str__(self):
        return self.name


from treebeard.mp_tree import MP_Node

class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)




class hier1(models.Model):
    Hierarchy_Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Hierarchy_Name



class Hier2(models.Model):
    hierarchy1 = models.ForeignKey(hier1,max_length=20, on_delete=models.CASCADE)
    Hierarchy_Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Hierarchy_Name


class Hier3(models.Model):
    hierarchy1 = models.ForeignKey(hier1, max_length=20, on_delete=models.CASCADE)
    hier2 = models.ForeignKey(Hier2, max_length=20, on_delete=models.CASCADE)
    hier3_name = models.CharField(max_length=50)

    def __str__(self):
        return self.hier3_name



class Hier4(models.Model):
    hierarchy1 = models.ForeignKey(hier1, max_length=20, on_delete=models.CASCADE)
    hier2 = models.ForeignKey(Hier2, max_length=20, on_delete=models.CASCADE)
    hier3 = models.ForeignKey(Hier3, max_length=20, on_delete=models.CASCADE)
    hier4_name = models.CharField(max_length=50)


    def __str__(self):
        return self.hier4_name


class Hier5(models.Model):
    hierarchy1 = models.ForeignKey(hier1, max_length=20, on_delete=models.CASCADE)
    hier2 = models.ForeignKey(Hier2, max_length=20, on_delete=models.CASCADE)
    hier3 = models.ForeignKey(Hier3, max_length=20, on_delete=models.CASCADE)
    hier4 = models.ForeignKey(Hier4, max_length=20, on_delete=models.CASCADE)
    hier5_name = models.CharField(max_length=20)

    def __str__(self):
        return self.hier5_name


from django.conf import settings
from django.db.models import ForeignKey, CASCADE, Model
from gst_field.modelfields import GSTField, PANField


from phone_field import PhoneField
class Customer(models.Model):
    CUSTOMER_CODE_CHOICE = (
        ('200253','200253'),
        ('200326','200326'),
        ('200385','200385'),
        ('200625','200625'),
        ('201184','201184'),
        ('201494','201494'),
        ('265848','265848'),
        ('266684','266684'),
        ('264104','264104'),
        ('264101','264101'),
    )
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    Customer_Code = models.PositiveIntegerField()
    Customer_Group = models.CharField(max_length=50, blank=True, null=True)
    City = models.CharField(max_length=50, blank=True, null=True)
    Pincode = models.CharField(max_length=10, null=True, blank=True)
    Contact_person_name = models.CharField(max_length=50, null=True, blank=True)
    GSTIN = GSTField()
    ZIN_NO = models.CharField(max_length=50, null=True, blank=True)
    Customer_Name = models.CharField(max_length=50, null=True, blank=True)
    State = models.CharField(max_length=50, null=True,blank=True)
    Address = models.TextField(max_length=250, null=True, blank=True)
    Contact_Number =PhoneField(blank=True, help_text='Contact phone number')
    Email_ID = models.EmailField(null=True, blank=True)
    PAN = PANField()
    Customer_For_Code =models.CharField(choices=CUSTOMER_CODE_CHOICE, max_length=10)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)




class Zone(models.Model):
    CHOICE = (
        ('Active','Active'),
        ('InActive', 'InActive'),
    )
    name = models.CharField(max_length=50)
    status = models.CharField(choices=CHOICE,max_length=10)

    def __str__(self):
        return self.name



class Distributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Distributor_Name = models.CharField(max_length=100, unique=True)
    Distributor_Code = models.CharField(max_length=25)
    Distributor_For_Code = models.CharField(max_length=30)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, blank=True)
    Region = models.CharField(max_length=25, null=True, blank=True)
    State = models.CharField(max_length=30, null=True, blank=True)
    City = models.CharField(max_length=30, null=True, blank=True)
    Address = models.TextField(max_length=500, null=True, blank=True)
    PinCode = models.PositiveIntegerField(max_length=6 , null=True, blank=True)
    Contact_Person_Name = models.CharField(max_length=100, null=True, blank=True)
    Contact_Number = models.PositiveIntegerField(max_length=50, null=True, blank=True)
    Email_ID = models.EmailField(max_length=100, null=True , blank=True)
    GSTIN = models.CharField(max_length=25, null=True, blank=True)
    DL_NO = models.CharField(max_length=100, null=True, blank=True)
    DL_NO_Valid_UPTO = models.DateTimeField(null=True, blank=True)
    PAN = models.CharField(max_length=15, null=True)
    TM_Email = models.EmailField(max_length=200,null=True, blank=True)
    RIS_Email = models.EmailField(max_length=200,null=True, blank=True)
    PS_Email = models.EmailField(max_length=200,null=True, blank=True)
    PSM_Email = models.EmailField(max_length=200,null=True, blank=True)
    ASM_Email = models.EmailField(max_length=200,null=True, blank=True)
    RSM_Email = models.EmailField(max_length=200,null=True,blank=True)
    BM_Email = models.EmailField(max_length=200,null=True, blank=True)
    SH_Email = models.EmailField(max_length=200,null=True, blank=True)
    BDM_Email = models.EmailField(max_length=200,null=True, blank=True)
    HO_Email = models.EmailField(max_length=200,null=True, blank=True)


    def __str__(self):
        return self.Distributor_Name





class Item(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    Item_Name = models.CharField(max_length=100)
    Item_Code = models.CharField(max_length=30)
    Batch_Enabled = models.CharField(max_length=20, null=True, blank=True)
    UOM = models.CharField(max_length=10)
    Principal_Company = models.CharField(max_length=100)
    MRP = models.PositiveBigIntegerField(null=True, blank=True)
    HSN_Code = models.CharField(max_length=5, null=True, blank=True)
    GST_Rate = models.FloatField(null=True, blank=True)
    GST_Applicable_From = models.DateTimeField(null=True, blank=True)
    hier1 = models.ForeignKey(hier1, on_delete=models.CASCADE)
    hier2 = models.ForeignKey(Hier2, on_delete=models.CASCADE)
    hier3 = models.ForeignKey(Hier3, on_delete=models.CASCADE)
    hier4 = models.ForeignKey(Hier4, on_delete=models.CASCADE)
    hier5 = models.ForeignKey(Hier5, on_delete=models.CASCADE)




class DetailSales(models.Model):
    Sales_Item_Code = models.ForeignKey(Item, on_delete=models.CASCADE)
    Sales_Quantity = models.PositiveIntegerField()
    Sales_Rate = models.DecimalField(max_digits=10, decimal_places=2)
    Sales_Serial_No = models.CharField(max_length=50)
    Sales_Batch = models.CharField(max_length=30, null=True, blank=True)
    Sales_Discount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    Total_Amount = models.DecimalField(max_digits=20, decimal_places=2)
    Reference_No = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.Sales_Quantity



class SalesTable(models.Model):
    Distributor_Code = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    Customer_Code = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Bill_Date = models.DateField()
    Invoice_No = models.CharField(max_length=50)
    Tally_MasterID = models.CharField(max_length=15, null=True, blank=True)
    Total_Inventory_Amount = models.DecimalField(max_digits=2,decimal_places=2, null=True, blank=True)
    Total_GST = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
    SGST_AMOUNT = models.DecimalField(max_digits=20,decimal_places=2 , null=True, blank=True)
    CGST_AMOUNT = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
    IGST_AMOUNT = models.DecimalField(max_digits=20,decimal_places=2, null=True, blank=True)
    Cash_Discount_Amount = models.DecimalField(max_digits=20,decimal_places=20, null=True, blank=True)
    R_O_Amount = models.DecimalField(max_digits=20,decimal_places=2,null=True, blank=True )
    Total_Invoice_Amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    @property
    def Total_Inventory_Amount(self):
        return "$%s" % self.Total_Inventory_Amount


    def __unicode__(self):
        return f'{self.Distributor_Code},{self.Customer_Code}'


