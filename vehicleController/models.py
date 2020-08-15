from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    logo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VehicleClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    model = models.CharField(max_length=150)
    year = models.CharField(max_length=4)
    engine = models.CharField(max_length=100)
    mileage = models.FloatField()
    class_type = models.ForeignKey(VehicleClass, related_name="vehicle_class", on_delete=models.CASCADE)
    v_type = models.ForeignKey(VehicleType, related_name="vehicle_type", on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, related_name="manufacturer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.model}"


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name="vehicle_images", on_delete=models.CASCADE)
    image = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle.name} - {self.image}"
    
    

    