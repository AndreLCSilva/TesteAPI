from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin


admin.site.register(NewUser)
