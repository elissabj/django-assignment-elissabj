from rest_framework import viewsets
from rest_framework import permissions
from disney.serializers import *

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer
    permission_classes = []

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer
    permission_classes = []


class DisneyCompanyViewSet(viewsets.ModelViewSet):
    queryset = DisneyCompany.objects.all()
    serializer_class = DisneyCompanySerializer
    permission_classes = []