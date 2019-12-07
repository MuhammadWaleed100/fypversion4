from django.db import models


class User(models.Model):
    uname=models.TextField()
    em=models.EmailField()
    pas=models.TextField()
    rad=models.TextField()