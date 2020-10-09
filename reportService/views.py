from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured


# Modelos
from django.contrib.auth.models import User, Group
# rest framework
from rest_framework import viewsets,status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

# serializers
from reportService.serializers import *

# metodos
class ReportViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    #pasamos los seriazer a cada metodo
    serializer_classes = {
        # 'list_reporting':reportSerializer,
        'saveReporting':reportSerializer,
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

        




#comprobar si el serializador sea una clase lo cual debe estar declarado en el serializador class
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()