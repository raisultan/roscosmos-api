from django.db import models
from django.utils.translation import gettext as _

from datetime import date


class LaunchPad(models.Model):
  name = models.CharField(max_length=255)
  establishment_date = models.DateField()
  location = models.CharField(max_length=255)
  area = models.CharField(max_length=64)
  rented = models.BooleanField(default=False)
  used_by = models.CharField(max_length=255, blank=True, null=True)
  use_period = models.CharField(max_length=255, blank=True, null=True)
  no_launches = models.IntegerField()
  no_employees = models.IntegerField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)


class SpaceTug(models.Model):
  name = models.CharField(max_length=255)
  manufacturer = models.CharField(max_length=255)
  first_launch_date = models.DateField(blank=True, null=True)
  autonomous_flight_time = models.CharField(max_length=64, blank=True, null=True)
  length = models.CharField(max_length=64)
  diameter = models.CharField(max_length=64)
  start_mass = models.CharField(max_length=64)
  fuel_type = models.CharField(max_length=64)
  fuel_supply = models.CharField(max_length=64)
  engine_thrust = models.CharField(max_length=64)
  no_inclusions = models.IntegerField()
  no_flights = models.IntegerField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)


class LaunchVehicle(models.Model):
  name = models.CharField(max_length=255)
  manufacturer = models.CharField(max_length=255)
  no_stages = models.IntegerField()
  length = models.CharField(max_length=64)
  diameter = models.CharField(max_length=64)
  start_mass = models.CharField(max_length=64)
  fuel_type = models.CharField(max_length=64)
  max_distance = models.CharField(max_length=64, blank=True, null=True)
  space_tugs = models.ManyToManyField(SpaceTug)
  STATUS_CHOICES = (
    ('ACTIVE', _('Действующий')),
    ('INACTIVE', _('Недействующий')),
  )
  status = models.CharField(max_length=12, choices=STATUS_CHOICES)
  description = models.TextField(blank=True, null=True)

class Launch(models.Model):
  name = models.CharField(max_length=255)
  date = models.DateField()
  time = models.TimeField()
  launch_pad = models.ForeignKey(LaunchPad, on_delete=models.CASCADE)
  launch_vehicle = models.ForeignKey(LaunchVehicle, on_delete=models.CASCADE)
  RESULT_CHOICES = (
    ('SUCCESS', _('Успешный')),
    ('FAILED', _('Неуспешный')),
    ('UPCOMING', _('Предстоящий')),
  )
  result = models.CharField(max_length=12, choices=RESULT_CHOICES)
  description = models.TextField(blank=True, null=True)


class Spacecraft(models.Model):
  name = models.CharField(max_length=255)
  manufacturer = models.CharField(max_length=255, blank=True, null=True)
  launch_mass = models.CharField(max_length=64)
  lifetime_period = models.CharField(max_length=64)
  orbital_period = models.CharField(max_length=64, blank=True, null=True)
  coverage_diameter = models.CharField(max_length=64, blank=True, null=True)
  power = models.CharField(max_length=64)
  launch_vehicles = models.ManyToManyField(LaunchVehicle)
  orbital_inclination = models.CharField(max_length=64, blank=True, null=True)
  accuracy = models.CharField(max_length=64, blank=True, null=True)
  description = models.TextField(blank=True, null=True)


class OrbitalGrouping(models.Model):
  name = models.CharField(max_length=255)
  first_launch_date = models.DateField(blank=True, null=True)
  no_spacecrafts = models.IntegerField(blank=True, null=True)
  spacecrafts = models.ManyToManyField(Spacecraft)
  no_planes = models.IntegerField(blank=True, null=True)
  no_spacecrafts_on_plane = models.IntegerField(blank=True, null=True)
  orbital_period = models.CharField(max_length=64, blank=True, null=True)
  orbital_inclination = models.CharField(max_length=64, blank=True, null=True)
  orbit_type = models.CharField(max_length=64)
  orbit_height = models.CharField(max_length=64, blank=True, null=True)
  accuracy = models.CharField(max_length=64, blank=True, null=True)
  coverage = models.CharField(max_length=64, blank=True, null=True)
  description = models.TextField(blank=True, null=True)


class SpaceObservatory(models.Model):
  name = models.CharField(max_length=255)
  manufacturer = models.CharField(max_length=255)
  launch_date = models.DateField()
  launch_pad = models.ForeignKey(LaunchPad, on_delete=models.CASCADE)
  launch_vehicles = models.ManyToManyField(LaunchVehicle)
  satellite_of = models.CharField(max_length=64)
  launch_mass = models.CharField(max_length=64)
  payload_mass = models.CharField(max_length=64)
  power = models.CharField(max_length=64)
  platform = models.CharField(max_length=255)
  power_source = models.CharField(max_length=64)
  lifetime_period = models.CharField(max_length=64)
  radio_frequency_range = models.CharField(max_length=64)
  transmission_speed = models.CharField(max_length=64)
  flight_duration = models.CharField(max_length=64)
  description = models.TextField(blank=True)


class SpaceStation(models.Model):
  name = models.CharField(max_length=255)
  spacecraft_type = models.CharField(max_length=64)
  launch_date = models.DateField()
  mass = models.CharField(max_length=64)
  length = models.CharField(max_length=64)
  width = models.CharField(max_length=64)
  pressurised_volume = models.CharField(max_length=64)
  atmospheric_pressure = models.CharField(max_length=64)
  perigee_altitude = models.CharField(max_length=64)
  apogee_altitude = models.CharField(max_length=64)
  orbital_inclination = models.CharField(max_length=64)
  orbital_speed = models.CharField(max_length=64)
  orbital_period = models.CharField(max_length=64)
  days_in_orbit = models.IntegerField()
  occupied_since = models.DateField()
  @property
  def days_occupied(self):
    current_date = date.today()
    delta = current_date - self.occupied_since
    return delta
  distance_traveled = models.CharField(max_length=64)
  power = models.CharField(max_length=64)
  revs_per_day = models.IntegerField()
  no_revs = models.IntegerField()
  curr_expedition = models.CharField(max_length=255)
  docked_spacecrafts = models.ManyToManyField(Spacecraft)
  main_modules = models.TextField()
  no_crew = models.IntegerField()
  description = models.TextField(blank=True)
