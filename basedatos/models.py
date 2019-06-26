from django.db import models

class Bienesyservicios(models.Model):
   idbs = models.AutoField(primary_key=True,verbose_name="ID bien y servicio")
   nombrebs = models.TextField(max_length=250,verbose_name="Nombre servicio")
   precio = models.DecimalField(max_digits=5, decimal_places=3)
   imgc = models.ImageField(upload_to='bysimg')
   fuente = models.URLField(max_length=200)
   fechas = models.DateField(verbose_name="Fecha de scraping")
   fechapub = models.DateField(verbose_name="Fecha de publicacion")
   id_cambio = models.ForeignKey('Tipocambio', on_delete=models.PROTECT)
   idreg = models.ForeignKey('Region',on_delete=models.PROTECT)
   idsubc = models.ForeignKey('Subcategoria', on_delete=models.PROTECT)

   class Meta:
       verbose_name = "Bienesyservicios"
       verbose_name_plural = 'Bienesyservicios'
       ordering = ["idbs"]

   def __str__(self):
       return self.idpais


class Region(models.Model):
   idreg = models.AutoField(primary_key=True)
   nombreg = models.TextField(max_length=200,verbose_name="Nombre Region")
   idpais = models.ForeignKey('Pais', on_delete=models.PROTECT)

   class Meta:
       verbose_name = "Region"
       verbose_name_plural = 'Regiones'
       ordering = ["idreg"]

   def __str__(self):
       return self.idpais

class Pais(models.Model):
   idpais = models.AutoField(primary_key=True,verbose_name="ID Pais")
   nombrep = models.TextField(max_length=100,blank=False,verbose_name="Nombre Pais")

   class Meta:
       verbose_name = "Pais"
       verbose_name_plural = 'Paises'
       ordering = ["idpais"]

   def __str__(self):
       return self.idpais

class Subcategoria(models.Model):
   idsubc = models.AutoField(primary_key=True)
   nomsc = models.TextField(max_length=200,verbose_name="Subcategoria")
   idcat = models.ForeignKey('Categoria', on_delete=models.PROTECT)

   class Meta:
       verbose_name = "Subcategoria"
       verbose_name_plural = 'Subcategorias'
       ordering = ["idcat"]

   def __str__(self):
       return self.nomsc

class Categoria(models.Model):
   idcat = models.AutoField(primary_key=True)
   nomcat = models.TextField(max_length=200,verbose_name="Categoria")

   class Meta:
       verbose_name = "Categoria"
       verbose_name_plural = 'Categorias'
       ordering = ["idcat"]

   def __str__(self):
       return self.nomcat



class Tipocambio(models.Model):
   id_cambio = models.AutoField(primary_key=True)
   nombrecamp = models.TextField(max_length=20,verbose_name="Moneda")
