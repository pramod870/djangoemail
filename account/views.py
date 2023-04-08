from django.shortcuts import render, reverse
from django.http import HttpResponse
from .forms import UserForm, DMFFORM, DMFFIELD
from .tasks import test_fun
from django.views.generic import CreateView
from .models import Sales
from .forms import CrispySaleForm
from django.contrib import messages
# Create your views here.





def test(request):
    test_fun.delay()
    return HttpResponse("Done")


def user_create(request):
    form = UserForm()
    return render(request, 'account/base.html',{'form':form})


def create_form(request):
    if request.method=="POST":
        form = DMFFIELD(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=DMFFIELD()
    return render(request,'account/form_create.html', {'form':form})





class CreateRegisterView(CreateView):
    model = Sales
    form_class = CrispySaleForm
    template_name = 'account/form_create.html'
    def form_valid(self, form):
        if self.request:
            form.instance = self.request
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse('text')



from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from .models import Question


class CreateView(generic.edit.CreateView):
    model = Question
    fields = ['question_text', 'pub_date']
    def get_form(self):
        form = super().get_form()
        form.fields['pub_date'].widget = DateTimePickerInput()
        return form
