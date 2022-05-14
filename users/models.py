from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    username = models.CharField(max_length=120)
    gh_username = models.CharField(max_length=120)
    email = models.EmailField
    bio = models.TextField()
    profile_pic_path = models.URLField()

