from django.db import models
from django.conf import settings
from ContactsApp.models import Contact

# Create your models here.
class UserContact(models.Model):
    codUserContact = models.AutoField(primary_key=True)
    idUser = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="ID de Usuario")
    idContact = models.OneToOneField(Contact,on_delete=models.CASCADE,limit_choices_to={'deleted':'false'},verbose_name="Contacto")
