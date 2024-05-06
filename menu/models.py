from django.db import models

# Create your models here.
class RegistroPedido(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('realizado', 'Realizado'),
    )
    cliente = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    productos_seleccionados = models.TextField()  # Campo para almacenar los productos seleccionados
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Registro - Cliente: {self.cliente}, Fecha: {self.fecha}, Total: {self.total}, Estado: {self.estado}"

    
class Platillos(models.Model):
    platillo_nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # Hacer el campo de imagen opcional
    precio_pequenio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    precio_mediano = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    precio_grande = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    
    # Agregar un índice al campo 'nombre' para búsquedas más rápidas
    class Meta:
        indexes = [
            models.Index(fields=['platillo_nombre']),
        ]

    def __str__(self):
        return self.platillo_nombre
    
class Bebidas(models.Model):
    bebida = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # Hacer el campo de imagen opcional
    precio_pequenio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    precio_mediano = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    precio_grande = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    
    # Agregar un índice al campo 'nombre' para búsquedas más rápidas
    class Meta:
        indexes = [
            models.Index(fields=['bebida']),
        ]

    def __str__(self):
        return self.bebida
    

class Aperitivos(models.Model):
    aperitivo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # Hacer el campo de imagen opcional
    precio_pequenio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    precio_mediano = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    precio_grande = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    
    # Agregar un índice al campo 'nombre' para búsquedas más rápidas
    class Meta:
        indexes = [
            models.Index(fields=['aperitivo']),
        ]

    def __str__(self):
        return self.aperitivo
    
class Galeria(models.Model):
    titulo = models.CharField(max_length=100)
    img = models.ImageField(upload_to='productos/galeria/', null=True, blank=True) 
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
    
