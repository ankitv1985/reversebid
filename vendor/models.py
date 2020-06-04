from django.db import models

# Create your models here.
class Vendor(models.Model):
    #['company_name', 'contact_person_name', 'contact_email', 'phone_number', 'category', 'days_of_payment']
    company_name = models.CharField(max_length=100,blank=False)
    contact_person_name = models.CharField(max_length=100,blank=False)
    contact_email = models.CharField(max_length=100,blank=False)
    phone_number = models.IntegerField(blank=False)


    CATEGORY_TYPE_CHOICES =(
        ('Furniture',"Furniture"),
        ('Stationary',"Stationary"),
        ('Surgical Instruments',"Surgical Instruments"),
        )
    category = models.CharField(
        max_length=100,
        choices = CATEGORY_TYPE_CHOICES,
        blank=False
        )

    days_of_payment = models.IntegerField(blank=False)

    class Meta:  
        db_table = "vendor"  