from django.contrib import admin

# Register your models here.
from .models import    RegistroPedido, Bebidas, Platillos, Aperitivos, Galeria

admin.site.register(Galeria)
admin.site.register(RegistroPedido)
admin.site.register(Bebidas)
admin.site.register(Platillos)
admin.site.register(Aperitivos)
