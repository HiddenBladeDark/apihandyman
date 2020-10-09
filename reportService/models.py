from django.db import models

class reporting(models.Model):
    idTecni = models.CharField(verbose_name='Identificacion tecnico', max_length=255, blank=False, null=False)
    idServi = models.CharField(verbose_name='Identificacion servicio', max_length=255,blank=False,null=False)
    datStart = models.DateTimeField(verbose_name='Fecha y hora de inicio', blank=True,null=False)
    datEnd = models.DateTimeField(verbose_name='Fecha y hora de finalizacion', blank=True,null=False)
    Descript = models.TextField(verbose_name='Descripcion', blank=False, null=False)

    def __str__(self):
        return str(self.idServi)