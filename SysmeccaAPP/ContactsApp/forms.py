from django.forms import (
    ModelForm, TextInput, Textarea, ClearableFileInput,
    EmailInput, URLInput, RadioSelect
    )
#from django import forms

from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact

        fields = ['listName','businessName','contactName','address1',
                  'address2','address3','address4','postCode',
                  'telephone','mobile','fax','email',
                  'website','categories','notes','picture']

        widgets = {
            'listName': TextInput(attrs={'class':'form-control','id':'listName','name':'listName','required':'','data-error':'Debe ingresar el Nombre de Lista'}),
            'businessName': TextInput(attrs={'class':'form-control','id':'businessName','name':'businessName'}),
            'contactName': TextInput(attrs={'class':'form-control','id':'contactName','name':'contactName','required':''}),
            'address1': TextInput(attrs={'class':'form-control','id':'address1','name':'address1','required':''}),
            'address2': TextInput(attrs={'class':'form-control','id':'address2','name':'address2'}),
            'address3': TextInput(attrs={'class':'form-control','id':'address3','name':'address3'}),
            'address4': TextInput(attrs={'class':'form-control','id':'address4','name':'address4'}),
            'postCode': TextInput(attrs={'class':'form-control','id':'postCode','name':'postCode'}),
            'telephone': TextInput(attrs={'class':'form-control','id':'telephone','name':'telephone'}),
            'mobile': TextInput(attrs={'class':'form-control','id':'mobile','name':'mobile'}),
            'fax': TextInput(attrs={'class':'form-control','id':'fax','name':'fax'}),
            'email': EmailInput(attrs={'class':'form-control','id':'email','name':'email'}),
            'website': URLInput(attrs={'class':'form-control','id':'website','name':'website'}),
            'categories': RadioSelect(attrs={'class':'radio','id':'categories','name':'categories'}),
            'notes': Textarea(attrs={'class':'form-control','id':'notes','name':'notes','rows':'8'}),
            'picture': ClearableFileInput(attrs={'name':'picture','id':'picture','style':'height:35px;'})
        }
