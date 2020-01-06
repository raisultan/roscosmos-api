from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('launchpads', views.LaunchPadViewSet)
router.register('spacetugs', views.SpaceTugViewSet)
router.register('launchvehicles', views.LaunchVehicleViewSet)
router.register('launches', views.LaunchViewSet)
router.register('spacecrafts', views.SpacecraftViewSet)
router.register('orbitalgroupings', views.OrbitalGroupingViewSet)
router.register('spaceobservatories', views.SpaceObservatoryViewSet)
router.register('spacestations', views.SpaceStationViewSet)

app_name = 'roscosmos'

urlpatterns = [
  path('', include(router.urls)),
]
