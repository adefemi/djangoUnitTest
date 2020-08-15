from django.urls import path, include
from .views import (
    VehicleClassView,
    VehicleImageView,
    ManufacturerView,
    VehicleView,
    VehicleTypeView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register("vehicles", VehicleView)
router.register("manufacturers", ManufacturerView)
router.register("vehicle-classes", VehicleClassView)
router.register("vehicle-types", VehicleTypeView)
router.register("vehicle-images", VehicleImageView)

urlpatterns = router.urls
