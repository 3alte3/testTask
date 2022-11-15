from django.db import models
from category.models import Category
from registration.models import NewUser


class Transaction(models.Model):
    amount = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    org = models.CharField(max_length=255)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True)
    type = models.CharField(choices=[('DE', 'Debiting'), ('RE', 'Replenishment')], max_length=255,null=True)
