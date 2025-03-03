from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    favorite_stocks = models.ManyToManyField('stocks.Stock', blank=True) 
    # favorite_stocks = ArrayField(models.CharField(max_length=10), blank=True, default=list)
    subscription_plan = models.CharField(
        max_length=10,
        choices=[('Free', 'Free'), ('Premium', 'Premium'), ('Pro', 'Pro')],
        default='Free'
    )

    def __str__(self):
        return self.username