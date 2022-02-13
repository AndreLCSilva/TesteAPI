from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pessoa.models import personData
from . serializers import personDataSerializer

@api_view(['GET', 'POST'])
def personData_list(request):
    if request.method == 'GET':
        pessoa = personData.objects.all()
        serializer = personDataSerializer(pessoa, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = personDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)