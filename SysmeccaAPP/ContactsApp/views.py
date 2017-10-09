from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection


from . models import Contact
from . forms import ContactForm
# Create your views here.

def contacslist(request):
    data = Contact.objects.all()
    return render(request,"ContactsApp/contacts_list.html",{"data":data})

def createcontact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            # Obtiene el archivo a subir (la imagen)
            contact.picture = request.FILES.get('picture')
            #Llamada al SP de insercion.
            with connection.cursor() as cursor:
                cursor.callproc('insert_contact',[contact.listName,contact.businessName,contact.contactName,contact.address1,
                                                  contact.address2,contact.address3,contact.address4,contact.postCode,
                                                  contact.telephone,contact.mobile,contact.fax,contact.email,contact.website,
                                                  contact.categories,contact.notes,0])
            # Obtener el elemento recien insertado
            # para enviarle al template el id y poder
            # almacenar correctamente la imagen del perfil.
            cont = Contact.objects.order_by('-idContact')[0]
            # asigna al nuevo objeto de tipo Contact el archivo a subir
            cont.picture = contact.picture
            contactAux = ContactForm(instance=cont)
            cont.save()

            messages.success(request, "Contacto creado satisfactoriamente")
            return redirect('contacts-details', id=cont.idContact)
        else:
            messages.error(request, "Error en los datos")
            form = ContactForm()            
    
    return render(request,"ContactsApp/contacts_new.html",{"form":form})

def contactdetails(request, id):
    data = Contact.objects.get(pk=id)
    return render(request,"ContactsApp/contacts_details.html",{"data":data})

def contactupdate(request, id):
    form = ContactForm()