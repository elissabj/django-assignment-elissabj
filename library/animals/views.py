from rest_framework import viewsets
from rest_framework import permissions
from library.animals.serializers import *

# Create your views here.
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = []

class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = []


class AnimalEnviViewSet(viewsets.ModelViewSet):
    queryset = AnimalEnvi.objects.all()
    serializer_class = AnimalEnviSerializer
    permission_classes = []