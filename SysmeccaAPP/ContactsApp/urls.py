from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.contacslist,name="contacts-list"),
    url(r'^nuevo/$',views.createcontact,name="contacts-new"),
    url(r'^detalles/(?P<id>[0-9]+)/$',views.contactdetails,name="contacts-details")
]