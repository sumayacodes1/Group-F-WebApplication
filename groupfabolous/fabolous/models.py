from django.db import models

class Department(models.Model):
    number = models.CharField(max_length=20)
    type = models.CharField(max_length=200)
    summary = models.CharField(max_length=50, default="No summary provided")




