from rest_framework import serializers
from .models import *

class AnimalSerializer (serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'verte_type', 'vital_function']

class EnvironmentSerializer (serializers.ModelSerializer):
    enviros = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Environment
        fileds = ['id', 'name_enviro', 'wildlife', 'descrip_enviro', 'enviros']

class AnimalEnviSerializer (serializers.ModelSerializer):
    class Meta:
        model = AnimalEnvi
        fields = ['id', 'animal', 'environment']
