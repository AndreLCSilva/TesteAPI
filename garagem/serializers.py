from rest_framework import serializers
from . models import Garagem

class garagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Garagem
        fields = ('garage_name', 'user_name')
