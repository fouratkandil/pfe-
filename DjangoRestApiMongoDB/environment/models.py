
from django.db import models

class Environment(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    type = models.CharField(max_length=200, blank=False, default='')
    location = models.CharField(max_length=200, blank=False, default='')