"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from pessoa.views import personData_list, personData_detail
from django.urls import path, include
from garagem.views import garagem_list
from api.views import clientes_cadastrados


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pessoa', personData_list.as_view()),
    path('api/pessoa/<int:pk>', personData_detail.as_view()),
    path('api/garagem', garagem_list.as_view()),
    path('api/options/', include('dj_rest_auth.urls')),
    path('api/register/', include('dj_rest_auth.registration.urls')),
    path('api/cadastrados', clientes_cadastrados),
]
