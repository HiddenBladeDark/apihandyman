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


import numpy as np
from datetime import datetime, timedelta


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



    @action(methods=['GET'],detail=False,url_path='calcHourJob/(?P<idTecni>[^/]+)/(?P<weekNum>\d+)')   
    def calcHourJob(self,request,idTecni,weekNum):
        # sacamos la semana
        weekCalc = reporting.objects.filter(idTecni=idTecni,datStart__week=weekNum,datEnd__week=weekNum)
        hour_tol = 0
        hour_norm = 0
        hour_noct = 0
        hour_dom = 0
        if weekCalc:
            serializer = self.get_serializer(weekCalc,many=True)
            datame =  json.loads(json.dumps(serializer.data))
            date_format = "%Y-%m-%d %H:%M:%S"
            for datas in datame:
                # pdas = np.arange(datas['datStart'], datas['datEnd'], dtype='datetime64')
                # print(pdas)
                start_date_time = datas['datStart'].replace('T',' ').replace('Z','')
                end_date_time = datas['datEnd'].replace('T',' ').replace('Z','')
                print(start_date_time)
                print(end_date_time)
                start_date_time = datetime.strptime(start_date_time, date_format)
                end_date_time = datetime.strptime(end_date_time, date_format)

                hour_tol += int(hourjobtol(start_date_time, end_date_time))
                hour_norm += int(hourjobnorm(start_date_time,end_date_time))
                hour_noct += int(hourjobnoct(start_date_time,end_date_time))
                hour_dom += int(hourjobdom(start_date_time,end_date_time))
            context = {
                'hour_tol':hour_tol,
                'hour_norm':hour_norm,
                'hour_noct':hour_noct,
                'hour_dom':hour_dom
            } 


            return Response(context,status=status.HTTP_200_OK)


        raise serializers.ValidationError({"error":"0"})




#comprobar si el serializador sea una clase lo cual debe estar declarado en el serializador class
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        else:
            return 0

        return super().get_serializer_class()



def hourjobtol(start,end):
    return abs(int((start-end).total_seconds())) / 3600


def hourjobnorm(start,end):
    print(start,' - ' ,end)
    # inicializamos variable tol
    tol = 0
     # dia de la semana sea menor a 6 por ser lunes a sabado 
    if start.weekday() <= 6:
        print(start.hour, ' - ', end.hour)
        # la hora sea mayor o igual a 7 y menor a 20
        if start.hour >= 7 and end.hour <= 20:
            # calculo de las horas que hay entre el rango de entrada
            tol += abs(int((start-end).total_seconds())) / 3600
            print(tol,'horas totales    ')
            return tol
        # total de horas mayor igual a 7
        if start.hour >= 7:
            # asignamos valor a horas de inicio
            hourstart = start.hour            
            # mientras la hora de inicio sea menor a 20
            while hourstart < 20:
                # contamos las horas de inicio hasta que llegue a 20
                hourstart += 1
                # horas transcurridas
                tol += 1
            print(tol,'horas trabajadas luego de las 20')
            # retornamos
            return tol
        # total de horas sea menor igual a 20
        if end.hour <= 20:
            # asignamos valor a las horas de inicio a 7
            hourstart = 7
            # mientras las horas de inicio sea menor a la hora final laborada
            while hourstart < end.hour:
                # contamos las horas de inicio hasta que llegue a la hora final
                hourstart += 1
                # horas transcurridas
                tol += 1
            print(tol,'horas trabajadas antes de las 20')
            # retornamos hora total
            return tol
        if start.hour <= 7 and end.hour >= 20:
            hourstart = 7
            while hourstart < 20:
                hourstart += 1
                tol += 1
            return tol
        else:
            return tol


# horas nocturnas
def hourjobnoct(start,end):
    print(start,' - ' ,end)
    # inicializamos variable tol
    tol = 0
    # dia de la semana sea menor a 6 por ser lunes a sabado 
    if start.weekday() <= 6:
        # print(start.hour, ' - ', end.hour)
        # horas laborales
        if start.hour >= 20 and end.hour <= 23:
            tol += abs(int((start-end).total_seconds())) / 3600
            # print(tol,'horas totales    ')
            # return tol 
            # print(tol,'hora luego de las 20')
            return tol
        if start.hour >= 0 and end.hour <= 7:
            tol += abs(int((start-end).total_seconds())) / 3600
            # print(tol,'horas totales    ')
            # return tol 
            # print(tol,'hora luego de las 20')
            return tol    
        if start.hour >= 0:
            hourstart = start.hour
            ehourend = end.hour
            # if end.hour >=20 and end.hour <= 23:
            #     print('entro')
            #     while ehourend < 23:
            #         ehourend += 1
            #         tol += 1
            #         print(tol)
            # else:
            while hourstart < 7:
                hourstart += 1
                tol += 1
            
        if end.hour >= 20 and end.hour <= 23:
            print('entro 1?')
            hourstart = 20
            ehourend = end.hour
            while hourstart < ehourend:
                hourstart += 1
                tol += 1              
        else:
            return tol
        return tol 
    else:
        return tol



        # if end.hour <= 7:
        #     # print('entra 2')
        #     # print(tol)
        #     hourstart = 0
        #     while hourstart < end.hour:
        #         hourstart += 1
        #         tol += 1
            # print(tol, ' horas nocturnas antes de las 7 am')
            # return tol
        # if end.hour <= 23:
        #     hourstart = 20
        #     if end.hour <= 7:
        #         # print('la hora es menor a 7')
        #         while hourstart < 23 :
        #             hourstart += 1
        #             tol += 1
        #         # print(tol,' hora nocturna despues de las 20 hasta las 24')
        #         # return tol
        #     else:
        #         # print('la hora es menor 24')
        #         while hourstart < 23:
        #             hourstart += 1
        #             tol += 1
        #         print(tol,' hora nocturna despues de las 20 hasta las 24')







def hourjobdom(start,end):
    # dia de la semana sea menor a 6 por ser lunes a sabado 
    if start.weekday() == 7:
        return abs(int((start-end).total_seconds())) / 3600 
    else:
        return 0