from django.db import models
# users
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nombrecompleto = models.CharField(max_length=254, verbose_name='Nombre completo', blank=False, null=False)
    identificopera = models.CharField(verbose_name='Identificacion operario',unique=True, max_length=254, blank=False, null=False)
    #establecemos el manejador de usuarios del modelo
    # USERNAME_FIELD = 'nombrecompleto'
    # REQUIRED_FIELDS = []
    def __str__(self):
        return str(self.identificopera)

class reporting(models.Model):
    idTecni = models.CharField(verbose_name='Identificacion tecnico', max_length=255, blank=False, null=False)
    idServi = models.CharField(verbose_name='Identificacion servicio', max_length=255,blank=False,null=False)
    datStart = models.DateTimeField(verbose_name='Fecha y hora de inicio', blank=True,null=False)
    datEnd = models.DateTimeField(verbose_name='Fecha y hora de finalizacion', blank=True,null=False)
    Descript = models.TextField(verbose_name='Descripcion', blank=False, null=False)

    def __str__(self):
        return str(self.idServi)

