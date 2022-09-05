from django.db import models
from django.contrib.auth.models import AbstractUser


class CostumUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=30)
