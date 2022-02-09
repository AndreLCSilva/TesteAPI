from rest_framework import generics
from pessoa.models import personData
from . serializers import personDataSerializer
from django.shortcuts import render, redirect

class pessoaAPIView(generics.ListAPIView):
    queryset = personData.objects.all()
    serializer_class = personDataSerializer

def submitPessoa(request):
    if request.POST:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        #usuario = request.user
        idUser = request.POST.get('idUser')
        if idUser:
            personData.objects.filter(idUser=idUser).update(name=name,
                                                      phone=phone,
                                                      email=email)
        else:
            personData.objects.create(name=name,
                                      phone=phone,
                                      email=email)
    return redirect('api/v1')