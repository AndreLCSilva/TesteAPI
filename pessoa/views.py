from rest_framework import generics, status
from rest_framework.response import Response
from . models import NewUser
from . serializers import personDataSerializer
from rest_framework.views import APIView
from rest_framework import status

class personData_list(APIView):
    def get(self, request, format=None):
        pessoa = NewUser.objects.all()
        serializer = personDataSerializer(pessoa, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = personDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class personData_detail(APIView):
    def get_object(self, pk):
        try:
            return NewUser.objects.get(pk=pk)
        except NewUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        pessoa = self.get_object(pk)
        serializer = personDataSerializer(pessoa)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        pessoa = self.get_object(pk)
        serializer = personDataSerializer(pessoa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        pessoa = self.get_object(pk)
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
