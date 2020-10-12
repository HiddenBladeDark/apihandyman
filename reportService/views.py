from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
import json

# Modelos
from django.contrib.auth.models import User, Group
# rest framework
from rest_framework import viewsets,status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
# serializers
from reportService.serializers import *

# datatime
import numpy as np
from datetime import datetime, timedelta
# script hour
from calchour import hourmethod

# metodos
class ReportViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    #pasamos los seriazer a cada metodo
    serializer_classes = {
        # 'list_reporting':reportSerializer,
        'saveReporting':reportSerializer,
        'calcHourJob':hourJobSerializer,
    }

    #listar roles 
    # @action(methods=['GET'],detail=False)
    # def list_reporting(self,request):
    #     # listamos todos
    #     reportings = reporting.objects.all()
    #     # pasamos el serializer convirtiendolo en json con many true
    #     serializer = self.get_serializer(reportings,many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    # # query set
    def get_queryset(self):
            return
    # guardar reporting
    @action(methods=['POST'],detail=False)
    def saveReporting(self,request):
        # obtenemos los datos obtenidos del request
        serializer = self.get_serializer(data=request.data)
        # validamos el serializer
        serializer.is_valid(raise_exception=True)
        #creamos el reporting
        reportings = reporting.objects.create(**serializer.validated_data)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


    # metodo para calc de las horas que sea por get y con parametros de entrada
    @action(methods=['GET'],detail=False,url_path='calcHourJob/(?P<idTecni>[^/]+)/(?P<weekNum>\d+)')   
    def calcHourJob(self,request,idTecni,weekNum):
        # filtramos una consulta para sacar el numero de la semana
        weekCalc = reporting.objects.filter(idTecni=idTecni,datStart__week=weekNum,datEnd__week=weekNum)
        # inicializamos variables
        tecniid = ''
        hour_tol = 0
        hour_norm = 0
        hour_noct = 0
        hour_dom = 0
        # si es verdadera la consulta
        if weekCalc:
            # llamar el serializer de calcHourJob de las class serializers
            serializer = self.get_serializer(weekCalc,many=True)
            # convertir los datos en json
            datame =  json.loads(json.dumps(serializer.data))
            # dar formato a las fecha ISO
            date_format = "%Y-%m-%d %H:%M:%S"
            # recorremos los datos obtenidos
            for datas in datame:
                # reemplazamos strings que haya en las fechas
                start_date_time = datas['datStart'].replace('T',' ').replace('Z','')
                end_date_time = datas['datEnd'].replace('T',' ').replace('Z','')
                # print(start_date_time)
                # print(end_date_time)
                # convertir los datos en tipo datetime
                start_date_time = datetime.strptime(start_date_time, date_format)
                end_date_time = datetime.strptime(end_date_time, date_format)
                # llamamos las funciones
                hour_tol += int(hourmethod.hourjobtol(start_date_time, end_date_time))
                hour_norm += int(hourmethod.hourjobnorm(start_date_time,end_date_time))
                hour_noct += int(hourmethod.hourjobnoct(start_date_time,end_date_time))
                hour_dom += int(hourmethod.hourjobdom(start_date_time,end_date_time))
                # dict para almacenar cada dato obtenido por parte de las funciones
            context = {
                'tecniid':idTecni,
                'hour_tol':hour_tol,
                'hour_norm':hour_norm,
                'hour_noct':hour_noct,
                'hour_dom':hour_dom
            } 
            # retornamos con los datos y estado completado
            return Response(context,status=status.HTTP_200_OK)
        # caso contrario
        context = {
            'tecniid':'Desconocido',
            'hour_tol':hour_tol,
            'hour_norm':hour_norm,
            'hour_noct':hour_noct,
            'hour_dom':hour_dom
        } 
        raise serializers.ValidationError(context)




#comprobar si el serializador sea una clase lo cual debe estar declarado en el serializador class
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        else:
            return 0

        return super().get_serializer_class()


