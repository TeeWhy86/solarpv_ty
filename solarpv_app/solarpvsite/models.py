from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=60)
    password = models.TextField(blank=True, null=True)
    first = models.TextField()
    middle = models.TextField()
    last = models.TextField()
    job = models.TextField()
    email = models.EmailField()
    office = models.TextField()
    cell = models.TextField()
    prefix = models.TextField()
    staff = models.TextField()
