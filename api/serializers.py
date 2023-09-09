from django.contrib.auth.models import User, Group
from rest_framework import serializers

from contato.models import Contato



class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ContatoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contato
        fields = '__all__'

