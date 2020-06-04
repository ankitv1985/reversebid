from django import forms
from .models import Vendor



class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        #fields = ('name', 'birthdate', 'brand', 'make')
        fields = ['company_name', 'contact_person_name', 'contact_email', 'phone_number', 'category', 'days_of_payment']
