from django.db import models

class food (models.Model):
    name= models.CharField (max_length=50)
    price= models.FloatField ()
    kilos= models.FloatField ()
    creation_date= models.DateField (auto_now_add=True)
    descrption= models.CharField (max_length=300, null= True, blank=True)

class drinks (models.Model):
    name= models.CharField (max_length=50)
    price= models.FloatField()
    gallons= models.FloatField()
    creation_date= models.DateField (auto_now_add=True)
    descrption= models.CharField (max_length=300, null= True, blank=True)

class freshfood (models.Model):
    name= models.CharField (max_length=50)
    price= models.FloatField ()
    kilos= models.FloatField ()
    creation_date= models.DateField (auto_now_add=True)
    rottendays= models.FloatField()
    descrption= models.CharField (max_length=300, null= True, blank=True)

