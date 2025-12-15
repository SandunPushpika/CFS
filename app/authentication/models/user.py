from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.timezone import now

class User(AbstractBaseUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User')
    ]
    role = models.CharField(choices=ROLE_CHOICES, max_length=20, default='false')
    degree = models.CharField(max_length=20)
    year_joined = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=now())
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    @property
    def current_academic_year(self):
        joined_year = self.year_joined.year
        return max(1, now().year - joined_year + 1)