from django.db import models

class Ram(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    capacidad = models.CharField(max_length=8)
    velocidad = models.CharField(max_length=10)
    estado = models.CharField(max_length=8)

class Notebook(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    procesador = models.CharField(max_length=15)
    ram = models.CharField(max_length=15)
    capacidad_ram = models.CharField(max_length=8)
    almacenamiento = models.CharField(max_length=15)
    tarjeta_video = models.CharField(max_length=15)
    estado_notebook = models.CharField(max_length=10)
    cargador_disponible = models.CharField(max_length=5)
    estado_bateria = models.CharField(max_length=10)

class Monitor(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=20)
    tamaño = models.IntegerField
    cargador = models.CharField(max_length=8)
    estado = models.CharField(max_length=8)

class Mouse(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=15)
    cableado = models.CharField(max_length=15)
    estado = models.CharField(max_length=8)

class Microfono(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=15)
    cableado = models.CharField(max_length=15)
    estado = models.CharField(max_length=8)

class Alcohol(models.Model):
    cantidad = models.IntegerField

class AireComprimido(models.Model):
    cantidad = models.IntegerField

class Switch(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=15)
    estado = models.CharField(max_length=8)

class Refrigeracion(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=15)
    sockets = models.CharField(max_length=40)
    tipo = models.CharField(max_length=30)


class PlacaBase(models.Model):
    marca = models.CharField(max_length=10)
    slots_memorias = models.CharField(max_length=10)
    modelo = models.CharField(max_length=15)
    sockets = models.CharField(max_length=40)
    chipset = models.CharField(max_length=30)
    formato = models.CharField(max_length=30)

class Teclado(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=15)
    cableado = models.CharField(max_length=15)
    estado = models.CharField(max_length=8)

class Adaptador(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=15)
    estado = models.CharField(max_length=8)

class DiscosExternos(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=15)
    capacidad = models.CharField(max_length=8)
    estado = models.CharField(max_length=8)