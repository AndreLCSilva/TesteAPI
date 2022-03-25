from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from rest_framework.authtoken.models import Token

class CustomAccountManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password, **other_fields):

        user_name = self.normalize_email(username)
        user = self.model(username=user_name, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(username, first_name, last_name, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    password2 = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username


# @receiver(post_save, sender=NewUser)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
