from django.db import models

class Bienesyservicios(models.Model):
   idbs = models.PositiveIntegerField(primary_key=True)
   nombrebs = models.TextField(max_length=250)
   precio = models.DecimalField(max_digits=5, decimal_places=3)
   imgc = models.ImageField(upload_to='bysimg')
   fuente = models.URLField(max_length=200)
   fechas = models.DateField()
   fechapub = models.DateField()
   id_cambio = models.ForeignKey('Tipocambio', on_delete=models.PROTECT)
   idreg = models.ForeignKey('Region',on_delete=models.PROTECT)
   idsubc = models.ForeignKey('Subcategoria', on_delete=models.PROTECT)

class Region(models.Model):
   idreg = models.PositiveIntegerField(primary_key=True)
   nombreg = models.TextField(max_length=200)
   idpais = models.ForeignKey('Pais', on_delete=models.PROTECT)

class Pais(models.Model):
   idpais = models.PositiveIntegerField(primary_key=True)
   nombrep = models.TextField(max_length=100)

class Subcategoria(models.Model):
   idsubc = models.PositiveIntegerField(primary_key=True)
   nomsc = models.TextField(max_length=200)
   idcat = models.ForeignKey('Categoria', on_delete=models.PROTECT)

class Categoria(models.Model):
   idcat = models.PositiveIntegerField(primary_key=True)
   nomcat = models.TextField(max_length=200)

class Tipocambio(models.Model):
   id_cambio = models.PositiveIntegerField(primary_key=True)
   nombrecamp = models.TextField(max_length=20)
