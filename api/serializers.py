from rest_framework import serializers
from pessoa.models import personData

class personDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = personData
        fields = ('name', 'phone', 'email', 'idUser')