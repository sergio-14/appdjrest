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
