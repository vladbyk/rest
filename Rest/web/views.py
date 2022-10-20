from rest_framework import viewsets
from .models import Person,Person1
from .serializers import PersonSerializers,Person1Serializers
from django.contrib.auth.models import User


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers

class Person1ViewSet(viewsets.ModelViewSet):
    queryset = Person1.objects.all()
    serializer_class = Person1Serializers
