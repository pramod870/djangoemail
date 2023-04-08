from django.contrib import admin

# Register your models here.

from .models import UserMaster, RoleMaster, MenuMaster, SubMenu, Student, DMFField, DMF, Sales, RegionMaster, \
    StateMaster, \
    CityMaster


class RegionAdmin(admin.StackedInline):
    model = RegionMaster
    fk_name = 'zone'


class StateAdmin(admin.StackedInline):
    model = StateMaster
    fk_name = 'region'


class CityAdmin(admin.ModelAdmin):
    inlines = [
        RegionAdmin,
        StateAdmin,
    ]


@admin.register(StateMaster)
class StateAdmin(admin.ModelAdmin):
    list_display = ('region', 'State_Name',)


@admin.register(CityMaster)
class CityAdmin(admin.ModelAdmin):
    list_display = ('State', 'City_Name',)


@admin.register(Sales)
class SalesMasterAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(UserMaster)
class UserMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'isauth', 'role',)


@admin.register(RoleMaster)
class RoleMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'description',)


@admin.register(MenuMaster)
class UserMasterAdmin(admin.ModelAdmin):
    list_display = ('Mid', 'MenuType', 'PMname', 'DisplayOrder', 'IsMobile',)
    # fieldsets = (
    #     ('Standard info', {
    #         'fields':('PMname',)
    #     }),
    #     (
    #         'Address info', {
    #             'fields': ('address',('DisplayOrder','MenuType',))
    #         }
    #     )
    # )


@admin.register(SubMenu)
class SbMasterAdmin(admin.ModelAdmin):
    list_display = ('SMid', 'Sname', 'DisplayOrder', 'IsMobile', 'menumaster', 'pagelinktype', 'pageLink')


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ('id', 'year_in_school',)


@admin.register(DMF)
class DMFAdmin(admin.ModelAdmin):
    list_display = ('form_name',)


@admin.register(DMFField)
class DMFieldAdmin(admin.ModelAdmin):
    list_display = ('field_name',)
