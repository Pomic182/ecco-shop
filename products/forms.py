from django import forms 

class Formulario_productos(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.FloatField ()
    kilos = forms.FloatField ()

class Formulario_drink(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.FloatField ()
    gallons = forms.FloatField ()

class Formulario_freshfood(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.FloatField()
    rottendays= forms.FloatField()

