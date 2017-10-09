from django.contrib import admin
from .models import Contact
# Register your models here.
class Contact_Admin(admin.ModelAdmin):
    list_display = ('idContact','contactName')

admin.site.register(Contact, Contact_Admin)