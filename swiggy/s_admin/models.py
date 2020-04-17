from django.db import models

class AdminLoginModel(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    otp = models.IntegerField()

