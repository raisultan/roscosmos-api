from rest_framework import viewsets, mixins

from . import serializers
from core.models import (LaunchPad,
                         SpaceTug,
                         LaunchVehicle,
                         Launch,
                         Spacecraft,
                         OrbitalGrouping,
                         SpaceObservatory,
                         SpaceStation)


class BasicViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin):
  pass


class LaunchPadViewSet(BasicViewSet):
  queryset = LaunchPad.objects.all()
  serializer_class = serializers.LaunchPadSerializer


class SpaceTugViewSet(BasicViewSet):
  queryset = SpaceTug.objects.all()
  serializer_class = serializers.SpaceTugSerializer


class LaunchVehicleViewSet(BasicViewSet):
  queryset = LaunchVehicle.objects.all()
  serializer_class = serializers.LaunchVehicleSerializer


class LaunchViewSet(BasicViewSet):
  queryset = Launch.objects.all()
  serializer_class = serializers.LaunchSerializer


class SpacecraftViewSet(BasicViewSet):
  queryset = Spacecraft.objects.all()
  serializer_class = serializers.SpacecraftSerializer


class OrbitalGroupingViewSet(BasicViewSet):
  queryset = OrbitalGrouping.objects.all()
  serializer_class = serializers.OrbitalGroupingSerializer


class SpaceObservatoryViewSet(BasicViewSet):
  queryset = SpaceObservatory.objects.all()
  serializer_class = serializers.SpaceObservatorySerializer


class SpaceStationViewSet(BasicViewSet):
  queryset = SpaceStation.objects.all()
  serializer_class = serializers.SpaceStationSerializer
