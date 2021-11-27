from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import list
from .forms import listForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = listForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = list.objects.all
            messages.success(request, ('Item has been added!') )
            return render(request, 'index.htm', {'all_items' : all_items})

    else:
        all_items = list.objects.all
        return render(request, 'index.htm', {'all_items':all_items})
