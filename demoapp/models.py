from django.db import models
class Todo(models.Model):
    task = models.CharField(max_length=30)
    discription = models.CharField(max_length=100)
