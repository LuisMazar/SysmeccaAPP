from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.signin, name="login"),
    url(r'^index/',views.index, name="index"),
]