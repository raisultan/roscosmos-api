from rest_framework import serializers

from core.models import (LaunchPad,
                         SpaceTug,
                         LaunchVehicle,
                         Launch,
                         Spacecraft,
                         OrbitalGrouping,
                         SpaceObservatory,
                         SpaceStation)


class LaunchPadSerializer(serializers.ModelSerializer):

  class Meta:
    model = LaunchPad
    fields = ('id', 'name', 'establishment_date', 'location',
              'area', 'rented', 'used_by', 'use_period',
              'no_launches', 'no_employees', 'description')
    read_only_fields = ('id', )


class SpaceTugSerializer(serializers.ModelSerializer):

  class Meta:
    model = SpaceTug
    fields = ('id', 'name', 'manufacturer', 'first_launch_date',
              'autonomous_flight_time', 'length', 'diameter',
              'start_mass', 'fuel_type', 'fuel_supply', 'engine_thrust',
              'no_inclusions', 'no_flights', 'description')
    read_only_fields = ('id', )


class LaunchVehicleSerializer(serializers.ModelSerializer):
  space_tugs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = LaunchVehicle
    fields = ('id', 'name', 'manufacturer', 'no_stages',
              'length', 'diameter', 'start_mass', 'fuel_type',
              'max_distance', 'space_tugs', 'status', 'description')
    read_only_fields = ('id', )


class LaunchSerializer(serializers.ModelSerializer):
  launch_pad = LaunchPadSerializer(read_only=True)
  launch_vehicle = LaunchVehicleSerializer(read_only=True)

  class Meta:
    model = Launch
    fields = ('id', 'name', 'date', 'time', 'launch_pad',
              'launch_vehicle', 'result', 'description')
    read_only_fields = ('id', )


class SpacecraftSerializer(serializers.ModelSerializer):
  launch_vehicles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = Spacecraft
    fields = ('id', 'name', 'manufacturer', 'launch_mass',
              'lifetime_period', 'orbital_period', 'coverage_diameter',
              'power', 'launch_vehicles', 'orbital_inclination',
              'accuracy', 'description')
    read_only_fields = ('id', )


class OrbitalGroupingSerializer(serializers.ModelSerializer):
  spacecrafts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = OrbitalGrouping
    fields = ('id', 'name', 'first_launch_date', 'no_spacecrafts',
              'spacecrafts', 'no_planes', 'no_spacecrafts_on_plane',
              'orbital_period', 'orbital_inclination', 'orbit_type',
              'orbit_height', 'accuracy', 'coverage', 'description')
    read_only_fields = ('id', )


class SpaceObservatorySerializer(serializers.ModelSerializer):
  launch_pad = LaunchPadSerializer(read_only=True)
  launch_vehicles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = SpaceObservatory
    fields = ('id', 'name', 'manufacturer', 'launch_date',
              'launch_pad', 'launch_vehicles', 'satellite_of',
              'launch_mass', 'payload_mass', 'power', 'platform',
              'power_source', 'lifetime_period', 'radio_frequency_range',
              'transmission_speed', 'flight_duration', 'description')
    read_only_fields = ('id', )


class SpaceStationSerializer(serializers.ModelSerializer):
  docked_spacecrafts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = SpaceStation
    fields = ('id', 'name', 'spacecraft_type', 'launch_date',
              'mass', 'length', 'width', 'pressurised_volume',
              'atmospheric_pressure', 'perigee_altitude',
              'apogee_altitude', 'orbital_inclination', 'orbital_speed',
              'orbital_period', 'in_orbit_since', 'days_in_orbit',
              'occupied_since', 'days_occupied', 'distance_traveled',
              'power', 'revs_per_day', 'no_revs', 'curr_expedition',
              'docked_spacecrafts', 'main_modules', 'no_crew', 'description')
    read_only_fields = ('id', )
