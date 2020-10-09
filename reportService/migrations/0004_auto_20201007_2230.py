# Generated by Django 3.1.2 on 2020-10-08 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportService', '0003_auto_20201007_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporting',
            name='Descript',
            field=models.TextField(default='xd', verbose_name='Descripcion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reporting',
            name='datEnd',
            field=models.DateTimeField(blank=True, verbose_name='Fecha y hora de finalizacion'),
        ),
        migrations.AlterField(
            model_name='reporting',
            name='datStart',
            field=models.DateTimeField(blank=True, verbose_name='Fecha y hora de inicio'),
        ),
        migrations.AlterField(
            model_name='reporting',
            name='idServi',
            field=models.CharField(max_length=255, verbose_name='Identificacion servicio'),
        ),
        migrations.AlterField(
            model_name='reporting',
            name='idTecni',
            field=models.CharField(max_length=255, verbose_name='Identificacion tecnico'),
        ),
    ]