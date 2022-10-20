from rest_framework import serializers
from .models import Person,Person1
from django.contrib.auth.models import User


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
class Person1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
