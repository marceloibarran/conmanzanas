from django.db import models
'''
class bienesyservicios(models.Model):
    idbs = models.PositiveIntegerField(primary_key=True)
    nombrebs  = models.TextField(max_length=250)
    precio = models.DecimalField(max_digits=5, decimal_places=3)
    imgc = models.ImageField(upload_to='bysimg')
    furnte = models.URLField(max_length=200)
    fechas = models.DateField()
    fechapub = models.DateField()
    id_cambio = models.ForeignKey(tipocambio)
    idreg = models.ManyToManyField(region)  #de n a n region y bienes y servicios
    idsubc = models.ForeignKey(subcategoria)



class region (models.Model):
    idreg = models.PositiveIntegerField(primary_key=True)
    nombreg = models.TextField(max_length=200)
    idpais = models.ForeignKey(pais)

class pais (models.Model):
    idpais = models.PositiveIntegerField(primary_key=True)
    nombrep = models.TextField(max_length=100)


class subcategoria (models.Model):
    idsubc = models.PositiveIntegerField(primary_key=True)
    nomsc = models.TextField(max_length=200)
    idcat = models.ForeignKey(categoria)

class categoria (models.Model):
    idcat = models.PositiveIntegerField(primary_key=True)
    nomcat = models.TextField(max_length=200)


class tipocambio(models.Model):
    id_cambio = models.PositiveIntegerField(primary_key=True)
    nombrecamp = models.TextField(max_length=20)

'''