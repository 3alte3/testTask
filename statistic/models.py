from django.db import models
from registration.models import NewUser


class UserStatistic(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    value = models.CharField(max_length=40)
