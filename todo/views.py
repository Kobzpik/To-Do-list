from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import list1
from .forms import listForm
from django.contrib import messages



# Create your views here.

def home(request): 
    
    
    if request.method == 'POST':
       
        form = listForm(request.POST or None)
        if form.is_valid():
            
            form.save()
            all_items = list1.objects.all()
            messages.success(request, ('Item has been added!') )
            
            return render(request, 'index.htm', {'all_items' : all_items} )

    else:
        all_items = list1.objects.all
        return render(request, 'index.htm', {'all_items':all_items})

#delete button funtion
def delete(request, pk):
    item = list1.objects.get(id=pk)
    item.delete()
    messages.success(request, ('Item has been Deleted!'))
    return redirect('/')

# cross off function
def cross(request, pk):
    item = list1.objects.get(id=pk)
    item.completed = True
    item.save()
    return redirect('/')

# uncross function
def uncross(request, pk):
    item = list1.objects.get(id=pk)
    item.completed = False
    item.save()
    return redirect('/')


#edit task
def edit(request ,pk):
    if request.method == 'POST':
        item = list1.objects.get(id=pk)

        form = listForm(request.POST or None , instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been Edited!'))
            return redirect('/')
    
    else:
        item = list1.objects.get(id=pk)
        return render(request , 'edit.htm', {'item' : item})


