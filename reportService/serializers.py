# lib auth and rest_framework
from django.contrib.auth.models import User, Group

from .models import *

from rest_framework import serializers

# convert json and xml


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class reportSerializer(serializers.ModelSerializer):
    # datStart = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y','iso-8601'])
    # datEnd = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y','iso-8601'])

    class Meta:
        model = reporting
        fields = '__all__'
    # validar fechas
    def validate(self,data):
        data = dict(data)
        print(data['datStart'])
        if (data['datStart'] > data['datEnd']):
            raise serializers.ValidationError({"error":"La fecha de inicio no puede ser mayor a la fecha de finalización"})
        return data

