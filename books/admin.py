from django.contrib import admin
from .models import Book, Tax,DocumentMasterType
# Register your models here.
@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('id','title','author','price','pages','book_type',)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('gstin','pan',)


@admin.register(DocumentMasterType)
class AdminDocumentType(admin.ModelAdmin):
    list_display = ('id','sales','salesreturn','name',)