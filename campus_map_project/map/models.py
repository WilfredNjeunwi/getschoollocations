from django.db import models

class CampusLocation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='location_images/')

    def __str__(self):
        return self.name
