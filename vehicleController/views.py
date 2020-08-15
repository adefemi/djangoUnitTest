from rest_framework.viewsets import ModelViewSet
from .serializer import *


class VehicleView(ModelViewSet):
    queryset = Vehicle.objects.select_related("v_type", "class_type", "manufacturer").prefetch_related("vehicle_images")
    serializer_class = VehicleSerializer


class ManufacturerView(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class VehicleTypeView(ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleClassView(ModelViewSet):
    queryset = VehicleClass.objects.all()
    serializer_class = VehicleClassSerializer


class VehicleImageView(ModelViewSet):
    queryset = VehicleImage.objects.all()
    serializer_class = VehicleImageSerializer
