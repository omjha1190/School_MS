from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    license_number = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to="driver/", null=True, blank=True)
    def __str__(self):
        return self.name


class Bus(models.Model):
    bus_number = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50)
    route = models.CharField(max_length=200)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.bus_number


        
    