from django.shortcuts import render
from . serializers import garagemSerializer
from . models import Garagem
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class garagem_list (APIView):
    def get(self, request, format=None):
        garagem = Garagem.objects.all()
        serializer = garagemSerializer(garagem, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = garagemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)