from rest_framework import serializers
from . models import NewUser

class personDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = ('id', 'first_name', 'last_name', 'user_name')