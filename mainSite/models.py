from django.db import models
# Create your models here.

class City(models.Model):
    name = models.TextField()
    state = models.TextField()
    lat = models.FloatField(verbose_name="latitude", null=True)
    lng = models.FloatField(verbose_name="longitude", null=True)
    costOfLiving = models.FloatField(null=True)

class Salary(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    occ_title = models.TextField()
    occ_code = models.TextField()
    h_median = models.FloatField(verbose_name="hourly median pay")
    a_median = models.FloatField(verbose_name="annual median pay")