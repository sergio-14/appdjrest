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
#mira mamá lo logre!!
def home(request):
    platillos = Platillos.objects.all()
    bebidas = Bebidas.objects.all()
    aperitivos = Aperitivos.objects.all()
    galeria = Galeria.objects.all()
    return render(request, 'home.html', {'platillos': platillos, 'bebidas': bebidas, 'aperitivos': aperitivos,'galeria': galeria})

def agregar_registro(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        cliente = request.POST.get('cliente')
        fecha = request.POST.get('fecha')
        total_str = request.POST.get('total')
        productos_seleccionados = request.POST.get('productos_seleccionados')
        
        # Intentar convertir el valor de total a un Decimal
        try:
            total = Decimal(total_str)
        except InvalidOperation as e:
            # Manejar el caso en que el valor de total no sea válido
            print(f"Error al convertir el valor de 'total' a Decimal: {e}")
            return HttpResponseNotFound("El valor de 'total' no es válido.")
        
        # Validar el valor de total para asegurarse de que sea positivo
        if total < Decimal('0.00'):
            raise ValidationError("El total debe ser un número decimal positivo.")
        
        # Crear una instancia del modelo Registro con los datos recibidos
        nuevo_registro = RegistroPedido(cliente=cliente, fecha=fecha, total=total, productos_seleccionados=productos_seleccionados)
        
        # Guardar el registro en la base de datos
        try:
            nuevo_registro.save()
            # Redireccionar al home en caso de éxito
            return redirect('home')
        except Exception as e:
            print(f"Error al guardar el registro en la base de datos: {e}")
            return HttpResponseNotFound("Error al guardar el registro en la base de datos.")
    
    else:
        # Manejar la solicitud GET de manera adecuada
        return HttpResponseNotFound("Esta página solo acepta solicitudes POST.")
    
def lista_pedidos(request):
    fecha_seleccionada = request.GET.get('fecha')
    lista_pedidos = RegistroPedido.objects.all().order_by('-fecha')

    total_ganado = 0  # Inicializar el total ganado
    
    if fecha_seleccionada:
        try:
            fecha_seleccionada = datetime.strptime(fecha_seleccionada, '%Y-%m-%d')
            lista_pedidos = lista_pedidos.filter(fecha__date=fecha_seleccionada)
            total_ganado = lista_pedidos.aggregate(total=Sum('total'))['total'] or 0
        except ValueError:
            pass # Si la fecha seleccionada no es válida, se ignora y se muestran todos los pedidos

    return render(request, 'lista_pedidos.html', {'pedidos': lista_pedidos, 'total_ganado': total_ganado, 'fecha_seleccionada': fecha_seleccionada})

def registrodia(request):
    fecha_actual = date.today()
    registros_pendientes = RegistroPedido.objects.filter(fecha__date=fecha_actual, estado='pendiente')

    if request.method == 'POST':
        registro_id = request.POST.get('registro_id')
        # Verificar si se presionó el botón para cambiar el estado
        if 'marcar_realizado' in request.POST:
            registro = RegistroPedido.objects.get(pk=registro_id)
            registro.estado = 'realizado'
            registro.save()
            return redirect('registrodia')  # Redirigir a la misma página después de cambiar el estado
        elif 'eliminar_registro' in request.POST:
            registro_id = request.POST.get('registro_id')
            registro = get_object_or_404(RegistroPedido, pk=registro_id)
            registro.delete()
            return redirect('registrodia')

    return render(request, 'registrodia.html', {'registros_pendientes': registros_pendientes})

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

