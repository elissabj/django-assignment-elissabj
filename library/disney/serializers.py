from rest_framework import serializers
from .models import *

class CompanySerializer (serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name_company', "year_creation"]

class MovieSerializer (serializers.ModelSerializer):
    companies = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Movie
        fileds = ['id', 'name', 'publish_year', 'hours', 'companies']

class DisneyCompanySerializer (serializers.ModelSerializer):
    class Meta:
        model = DisneyCompany
        fields = ['id', 'movie', 'company']

