from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='name')
    surname = models.CharField(max_length=100, default='surname')
    email = models.EmailField(max_length=255, default='email')
    
    def __str__(self):
        return self.user.username