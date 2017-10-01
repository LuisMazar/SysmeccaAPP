from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login_(request):
    if not request.user.is_anonymous():
        return redirect("https://www.google.com")
    
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            user = request.POST['username']
            key = request.POST['password']
            acceso = authenticate(username=user, password=key)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    #qs = User.objects.get(username=user)
                    #usr =
                    messages.success(request, 'Bienvenido '+user)
                    return redirect("index")
                else:
                    messages.error(request,'El Usuario no esta activo. Por favor, contactarse con el administrador, para resolver el problema')
                    form = AuthenticationForm()
            else:
                messages.error(request,'Error de acceso. El Usuario y contrasena no coinciden o no existen')
                form = AuthenticationForm()
    else:
        form = AuthenticationForm()

    return render(request,"Login.html",{'form':form})

def index(request):
    msg = "Hola si funciona"
    return render(request,"index.html",{"msg":msg})