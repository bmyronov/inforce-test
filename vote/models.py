from django.db import models
from django.utils import timezone


class Vote(models.Model):
    menu = models.IntegerField()
    likes = models.IntegerField(default=0)
    date = models.DateField(default=timezone.localdate)
