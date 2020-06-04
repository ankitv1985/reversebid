from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Vendor
from .forms import VendorForm


def vendorfunc(request):  
    if request.method == "POST":  
        form = VendorForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('/show')  
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'show">reload</a>""")
            #return redirect('/emp')

    else:  
        form = VendorForm()
        #return render(request,'show.html') 
        return render(request,'vendor.html',{'form':form})

def showfunc(request):  
    vendors = Vendor.objects.all()  
    return render(request,'show.html',{'vendors':vendors})
