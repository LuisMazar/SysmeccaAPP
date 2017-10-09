from django.db import models

# Create your models here.

categories_list = (
    ('cl','Club'),
    ('fr','Amigo'),
    ('su','Proveedor'),
    ('wo','Taller'),
)

def upload_location(instance, filename):
    return "%s/%s" %(instance.idContact, filename)

class Contact (models.Model):
    idContact = models.AutoField(primary_key=True)
    listName = models.CharField(max_length=50, verbose_name="Nombre de Lista")
    businessName = models.CharField(max_length=50, null=True, blank=True, verbose_name="Nombre de Negocios")
    contactName = models.CharField(max_length=50, verbose_name="Nombre de Contacto")
    address1 = models.CharField(max_length=250, verbose_name="Direccion 1")
    address2 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Direccion 2")
    address3 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Direccion 3")
    address4 = models.CharField(max_length=250, null=True, blank=True, verbose_name="Direccion 4")
    postCode = models.CharField(max_length=10, null=True, blank=True, verbose_name="Codigo Postal")
    telephone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Teléfono")
    mobile = models.CharField(max_length=20, null=True, blank=True, verbose_name="Celular")
    fax = models.CharField(max_length=20, null=True, blank=True, verbose_name="Fax")
    email = models.EmailField(verbose_name="Correo Electrónico", null=True, blank=True)
    website = models.URLField(verbose_name="Sitio Web", null=True, blank=True)
    categories = models.CharField(max_length=50, null=True, blank=True, choices=categories_list, verbose_name="Categorias")
    notes = models.TextField(verbose_name="Notas", null=True, blank=True)
    deleted = models.BooleanField(verbose_name="Eliminado")
    #contactType = 
    picture = models.ImageField(verbose_name="Imagen", max_length=400, null=True, blank=True, upload_to=upload_location)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now = True)

    def __str__(self):
        return str(self.idContact)

