from .models import *
from rest_framework import serializers


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Manufacturer


class VehicleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = VehicleType


class VehicleClassSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = VehicleClass


class VehicleImageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = VehicleImage


class VehicleSerializer(serializers.ModelSerializer):
    vehicle_images = VehicleImageSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)
    v_type = VehicleTypeSerializer(read_only=True)
    class_type = VehicleClassSerializer(read_only=True)

    class Meta:
        fields = "__all__"
        model = Vehicle