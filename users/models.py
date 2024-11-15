from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True, unique=True )
    email = models.EmailField(unique=True)
    role = models.CharField(default='user')

    USERNAME_FIELD = 'email'  # Set email as the unique identifier for authentication
    REQUIRED_FIELDS = [] 
