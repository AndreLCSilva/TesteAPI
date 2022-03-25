from django.shortcuts import render
import requests

def clientes_cadastrados(request):
    queryset = requests.get("http://127.0.0.1:8000/api/pessoa", headers={"Authorization" : "Token f8cd01852c66a5d5dd2125644b5675e277bd9e24"}).json()
    return render(request, "pessoas.html", {'queryset' : queryset})