from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # Add your custom fields here
    user_type = models.CharField(max_length=15)
