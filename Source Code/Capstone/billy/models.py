from django.db import models

# Create your models here.
class complaints(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    incident_type = models.CharField(max_length=50)
    incident_description = models.CharField(max_length=500)
    evidence = models.FileField()