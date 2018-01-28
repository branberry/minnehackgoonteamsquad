from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    user_id = models.IntegerField()
    bucket_name = models.CharField(max_length=200)

class Injury(models.Model):
    user_id = models.IntegerField()
    injury_type = models.CharField(max_length=200)
    symptoms = models.CharField(max_length=400)
    bench_date = models.DateTimeField('date benched')
    unbench_date = models.DateTimeField('date unbenched')
