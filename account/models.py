from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class RoleMaster(models.Model):
    STUDENT = 1
    TEACHER = 2
    SECRETARY = 3
    SUPERVISOR = 4
    ADMIN = 5
    ABS = 6
    CS = 7
    ND = 8
    PD = 9
    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (SECRETARY, 'secretary'),
        (SUPERVISOR, 'supervisor'),
        (ADMIN, 'admin'),
        (ABS, 'abs'),
        (CS, 'cs'),
        (ND, 'ND'),
        (PD, 'pd'),

    )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.get_id_display()


class UserMaster(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=50)
    isauth = models.BooleanField(default=False)
    role = models.OneToOneField(RoleMaster, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username


class MenuMaster(models.Model):
    Mid = models.AutoField(primary_key=True)
    MenuType = models.CharField(max_length=100, null=True)
    PMname = models.CharField(max_length=100)
    DisplayOrder = models.CharField(max_length=100, null=True)
    IsMobile = models.BooleanField(default=False)
    IconImage = models.ImageField(upload_to='MenuImages', null=True)

    def __str__(self):
        return self.PMname


class SubMenu(models.Model):
    PAGE_LINK_TYPE = (
        ('Report', 'Report'),
        ('static', 'static'),
        ('Master', 'Master'),
        ('Document', 'Document'),
        ('DReport', 'DReport'),
        ('Calendar', 'Calendar'),
        ('MasterCalendar', 'MasterCalender'),

    )
    PAGE_LINK = (
        ('Bill Wise Sales Report', 'Bill Wise Sales Report'),
        ('Bill Wise Sales Report Detailed', 'Bill Wise Sales Report Detailed'),
        ('Bill Wise Sales Report old', 'Bill Wise Sales Report old'),
        ('Access Control', 'Access Control'),
        ('Asign Users', 'Asign Users'),
        ('Consolidated Sync Report Admin', 'Consolidated Sync Report Admin'),
        ('Dashboad Config', 'Dashboad Config'),
        ('Distributor MIS Report', 'Distributor MIS Report'),
        ('Document Upload', 'Document Uploader'),
        ('Dynamic Forms', 'Dynamic Forms'),
        ('Dynamic Work Flow', 'Dynamic Work Flow'),
        ('Error', 'Error'),
        ('Explorer', 'Explorer'),
        ('FTP', 'FTP'),
        ('Holiday', 'Holiday'),
        ('Invoice Explorer', 'Invoice Explorer'),
        ('Kill Request', 'Kill Request'),
        ('LastTransactionReportLog', 'LastTransactionReportLog'),
        ('Location', 'Location'),
        ('Manage Account', 'Manage Account'),
        ('Master Map Settings', 'Master Map Settings'),
        ('Menu Control', 'Menu Control'),

    )

    SMid = models.AutoField(primary_key=True)
    Sname = models.CharField(max_length=100)
    DisplayOrder = models.CharField(max_length=100, null=True)
    IsMobile = models.BooleanField(default=False)
    IconImage = models.ImageField(upload_to="SubMenuImages", null=True)
    pagelinktype = models.CharField(max_length=50, choices=PAGE_LINK_TYPE)
    pageLink = models.CharField(max_length=50, choices=PAGE_LINK)
    menumaster = models.ForeignKey(MenuMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.Sname


class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}


class DMFField(models.Model):
    field_name = models.CharField(max_length=500)


class DMF(models.Model):
    form_name = models.CharField(max_length=500)
    fields = models.ForeignKey(DMFField, on_delete=models.CASCADE)


class Sales(models.Model):
    name = models.CharField(max_length=40)
    Bill_Date = models.DateField()
    Invoice_No = models.CharField(max_length=50)
    Tally_MasterID = models.CharField(max_length=15, null=True, blank=True)
    Total_Inventory_Amount = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)
    Total_GST = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    SGST_AMOUNT = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)


import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('polls:detail', kwargs={'pk': self.pk})


class RegionMaster(models.Model):
    Region_Name = models.CharField(max_length=50, verbose_name='Region Name')

    def __str__(self):
        return self.Region_Name


class StateMaster(models.Model):
    region = models.ForeignKey(RegionMaster, on_delete=models.CASCADE)
    State_Name = models.CharField(max_length=50, verbose_name="State Name")

    def __str__(self):
        return self.State_Name


class CityMaster(models.Model):
    State = models.ForeignKey(StateMaster, on_delete=models.CASCADE)
    City_Name = models.CharField(max_length=50, verbose_name="City Name")

    def __str__(self):
        return self.City_Name
