from django import forms
from .models import Book, DocumentMasterType

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )


import django_tables2 as tables


class SimpleTable(tables.Table):
    class Meta:
        model = Book



