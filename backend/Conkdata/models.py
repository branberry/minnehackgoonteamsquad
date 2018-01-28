from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    user_id = models.IntegerField()

class Injury(models.Model):
    user_id = models.IntegerField()
    injury_type = models.CharField(max_length=200)
    symptoms = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
