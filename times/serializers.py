from rest_framework import serializers
from .models import * 

class TimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['id','times'] 

class CaracteriticasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Caracteristicas
        fields = ['id', 'estadio', 'cidade', 'times']
        