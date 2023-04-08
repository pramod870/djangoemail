from django.contrib import admin
from .models import (dummy, Genre, Category, hier1, Hier2, Hier3, Hier4, Hier5,
                       Customer, Item, Distributor, Zone, DetailSales, SalesTable)
# Register your models here.
from django.contrib.admin import SimpleListFilter
from import_export.fields import Field






@admin.register(dummy)
class AdminDummy(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ('name','parent',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)





#
@admin.register(hier1)
class Hierarchy1Admin(admin.ModelAdmin):
    list_display = ('Hierarchy_Name',)

@admin.register(Hier2)
class Hierarchy2Admin(admin.ModelAdmin):
    list_display = ('Hierarchy_Name',)


@admin.register(Hier3)
class Hierarchy3Admin(admin.ModelAdmin):
    list_display = ('hier3_name',)


@admin.register(Hier4)
class Hierarchy4Admin(admin.ModelAdmin):
    list_display = ('hier4_name',)

@admin.register(Hier5)
class Hierarchy5Admin(admin.ModelAdmin):
    list_display = ('hier5_name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','Customer_Name','Customer_Code',]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','Item_Code','Batch_Enabled','UOM','Principal_Company','MRP','HSN_Code','GST_Rate','GST_Applicable_From']


@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ['user','Distributor_Name','Distributor_Code']


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['name']




@admin.register(SalesTable)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['Distributor_Code','Customer_Code']


@admin.register(DetailSales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['Sales_Quantity']