from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from .models import RegistroPedido, Platillos, Bebidas, Aperitivos,Galeria
from decimal import Decimal,InvalidOperation
from django.http import HttpResponseNotFound
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, date
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
#inicio
def home (request):
    return render(request, 'home.html')


def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'POST':
        # Obtiene el username y la contraseña del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autentica al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si el usuario es autenticado correctamente, inicia sesión
            login(request, user)
            # Redirige al usuario a algún lugar, por ejemplo, al dashboard
            return redirect('home')
        else:
            # Si la autenticación falla, muestra un mensaje de error
            error_message = "Usuario y/o contraseña incorrectos."
            return render(request, 'signin.html', {'error_message': error_message})

    # Si la solicitud no es POST, simplemente renderiza el formulario vacío
    return render(request, 'signin.html')

