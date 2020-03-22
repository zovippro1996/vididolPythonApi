from django.contrib.auth.models import User
from rest_framework import serializers
from backendPy.webserviceapi.models import User, Star

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class StarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Star
        fields = ('username', 'is_certified', 'response', 'response_rate')
