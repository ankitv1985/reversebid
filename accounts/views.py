from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def indexView(request):
    return render(request,'accounts/home.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = SignUpForm()

    return render(request,'registration/register.html',{'form':form})



'''class VendorCreateView(CreateView):
    model = Vendor
    form_class = VendorForm
    success_url = reverse_lazy('person_changelist')'''

'''def load_make(request):
    brand_id = request.GET.get('brand')
    make = Make.objects.filter(brand_id=brand_id).order_by('name')
    return render(request, 'personal/make_dropdown_list_options.html', {'make': make})'''


'''class VendorListView(ListView):
    model = Person
    context_object_name = 'people'
    '''