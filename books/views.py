from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/user_list.html', {'books': books})



# def book_create(request):
#     form = BookForm()
#     context = {'form': form}
#     html_form = render_to_string('books/partial_user_create.html',
#         context,
#         request=request,
#     )
#     return JsonResponse({'html_form': html_form})
#
# def book_create(request):
#     data = dict()
#
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#         else:
#             data['form_is_valid'] = False
#     else:
#         form = BookForm()
#
#     context = {'form': form}
#     data['html_form'] = render_to_string('books/includes/partial_user_create.html',
#         context,
#         request=request
#     )
#     return JsonResponse(data)

# def book_create(request):
#     data = dict()
#
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#             books = Book.objects.all()
#             data['html_book_list'] = render_to_string('books/partial_user_list.html', {
#                 'books': books
#             })
#         else:
#             data['form_is_valid'] = False
#     else:
#         form = BookForm()
#
#     context = {'form': form}
#     data['html_form'] = render_to_string('books/partial_user_create.html',
#         context,
#         request=request
#     )
#     return JsonResponse(data)

###########################

def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('books/partial_user_list.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()
    return save_book_form(request, form, 'books/partial_user_create.html')


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return save_book_form(request, form, 'books/partial_user_update.html')


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        books = Book.objects.all()
        data['html_book_list'] = render_to_string('books/partial_user_list.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('books/partial_user_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


def pie_chart(request):
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi",
             "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render('piechart.html', data)


import django_tables2 as tables
from .forms import SimpleTable
from django_tables2.export.views import ExportMixin
class TableView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = Book.objects.all()
    template_name = "books/simple_list.html"


from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport

from .models import Book
from .forms import SimpleTable
def table_view(request):
    table = SimpleTable(Book.objects.all())
    RequestConfig(request).configure(table)

    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("table.{}".format(export_format))
    return render(request, "table.html", {
        "table": table
    })