
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.

class User(AbstractBaseUser):
  username = models.CharField(max_length=100,unique=True)
  email = models.EmailField(max_length=100,unique=True)
  is_blocked = models.BooleanField(default=False)
  is_administrator = models.BooleanField(default=False)

  USERNAME_FIELD='email'

