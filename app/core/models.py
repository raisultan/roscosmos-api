from django.db import models
from django.utils.translation import gettext as _

from datetime import date


class LaunchPad(models.Model):
  name = models.CharField(max_length=255)
  establishment_date = models.DateField()
  location = models.CharField(max_length=255)
  area = models.CharField(max_length=64)
  rented = models.BooleanField(default=False)
  used_by = models.CharField(max_length=255, blank=True)
  use_period = models.CharField(max_length=255, blank=True)
  no_launches = models.IntegerField()
  no_employees = models.IntegerField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  image = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.name


class SpaceTug(models.Model):
  name = models.CharField(max_length=255)
  manufacturer = models.CharField(max_length=255)
  first_launch_date = models.DateField(blank=True, null=True)
  autonomous_flight_time = models.CharField(max_length=64, blank=True)
  length = models.CharField(max_length=64)
  diameter = models.CharField(max_length=64)
  start_mass = models.CharField(max_length=64)
  fuel_type = models.CharField(max_length=64)
  fuel_supply = models.CharField(max_length=64)
  engine_thrust = models.CharField(max_length=64)
  no_inclusions = models.IntegerField(blank=True, null=True)
  no_flights = models.IntegerField(blank=True, null=True)
  description = models.TextField(blank=True)
  image = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.name


class LaunchVehicle(models.Model):
  name = models.CharField(max_length=255)
  manufacturer = models.CharField(max_length=255)
  no_stages = models.IntegerField()
  length = models.CharField(max_length=64)
  diameter = models.CharField(max_length=64)
  start_mass = models.CharField(max_length=64)
  fuel_type = models.CharField(max_length=64)
  max_distance = models.CharField(max_length=64, blank=True)
  space_tugs = models.ManyToManyField(SpaceTug, blank=True)
  no_launches = models.IntegerField(blank=True, null=True)
  STATUS_CHOICES = (
    ('ACTIVE', _('Действующий')),
    ('INACTIVE', _('Недействующий')),
  )
  status = models.CharField(max_length=12, choices=STATUS_CHOICES)
  description = models.TextField(blank=True, null=True)
  image = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.name


class Launch(models.Model):
  name = models.CharField(max_length=255)
  date = models.DateField()
  time = models.TimeField(null=True)
  launch_pad = models.ForeignKey(LaunchPad, on_delete=models.CASCADE)
  launch_vehicle = models.ForeignKey(LaunchVehicle, on_delete=models.CASCADE)
  RESULT_CHOICES = (
    ('EMERGENCY', _('Аварийный')),
    ('SUCCESS', _('Успешный')),
    ('FAILED', _('Неуспешный')),
    ('UPCOMING', _('Предстоящий')),
  )
  result = models.CharField(max_length=12, choices=RESULT_CHOICES)
  description = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.name


class Spacecraft(models.Model):
  name = models.CharField(max_length=255)
  manufacturer = models.CharField(max_length=255, blank=True)
  launch_mass = models.CharField(max_length=64)
  lifetime_period = models.CharField(max_length=64)
  orbital_period = models.CharField(max_length=64, blank=True)
  coverage_diameter = models.CharField(max_length=64, blank=True)
  power = models.CharField(max_length=64, blank=True)
  launch_vehicles = models.ManyToManyField(LaunchVehicle, blank=True)
  orbital_inclination = models.CharField(max_length=64, blank=True)
  accuracy = models.CharField(max_length=64, blank=True)
  description = models.TextField(blank=True)
  image = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.name


class OrbitalGrouping(models.Model):
  name = models.CharField(max_length=255)
  first_launch_date = models.DateField(blank=True, null=True)
  no_spacecrafts = models.IntegerField(blank=True, null=True)
  spacecrafts = models.ManyToManyField(Spacecraft)
  no_planes = models.IntegerField(blank=True, null=True)
  no_spacecrafts_on_plane = models.IntegerField(blank=True, null=True)
  orbital_period = models.CharField(max_length=64, blank=True)
  orbital_inclination = models.CharField(max_length=64, blank=True)
  orbit_type = models.CharField(max_length=64)
  orbit_height = models.CharField(max_length=64, blank=True)
  accuracy = models.CharField(max_length=64, blank=True)
  coverage = models.CharField(max_length=64, blank=True)
  description = models.TextField(blank=True)
  image = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.name


class SpaceObservatory(models.Model):
  name = models.CharField(max_length=255)
  manufacturer = models.CharField(max_length=255)
  launch_date = models.DateField()
  launch_time = models.TimeField()
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
  image = models.URLField(null=True, blank=True)

  @property
  def flight_duration(self):
    current_date = date.today()
    delta = current_date - self.launch_date
    return delta.days
  description = models.TextField(blank=True)

  def __str__(self):
    return self.name


class SpaceStation(models.Model):
  name = models.CharField(max_length=255)
  spacecraft_type = models.CharField(max_length=64)
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
  occupied_since = models.DateField()
  in_orbit_since = models.DateField()

  @property
  def days_in_orbit(self):
    current_date = date.today()
    delta = current_date - self.in_orbit_since
    return delta.days

  @property
  def days_occupied(self):
    current_date = date.today()
    delta = current_date - self.occupied_since
    return delta.days
  distance_traveled = models.CharField(max_length=64)
  power = models.CharField(max_length=64)
  curr_expedition = models.CharField(max_length=255)
  docked_spacecrafts = models.ManyToManyField(Spacecraft, blank=True)
  main_modules = models.TextField()
  no_crew = models.IntegerField()
  description = models.TextField(blank=True)
  image = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.name


class ParseUrl(models.Model):
  name = models.CharField(max_length=255)
  url = models.URLField()
  description = models.TextField(blank=True)

  def __str__(self):
    return self.name


class ParserLaunch(models.Model):
  url = models.ForeignKey(ParseUrl, on_delete=models.CASCADE)
  parse_date = models.DateTimeField(auto_now_add=True)
  no_launches_saved = models.IntegerField()
  last_saved_launch_no = models.IntegerField()

  def __str__(self):
    return f'{self.parse_date}'
