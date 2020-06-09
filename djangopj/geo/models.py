from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Country(models.Model):
  name = models.CharField(max_length=255, db_index=True)
  key = models.CharField(max_length=2, db_index=True)
  created_at = models.DateTimeField(db_index=True, auto_now_add=True, null=True)
  modified_at = models.DateTimeField(db_index=True, auto_now=True, null=True)

  class Meta:
    verbose_name_plural = "countries"

  def publish(self):
      self.modified_at = timezone.now()
      self.save()

  def __str(self):
      return self.name


class Prefecture(models.Model):
  name = models.CharField(max_length=255, db_index=True)
  key = models.CharField(max_length=255, db_index=True)
  country = models.ForeignKey(Country, on_delete=models.PROTECT, db_index=True)
  created_at = models.DateTimeField(db_index=True, auto_now_add=True, null=True)
  modified_at = models.DateTimeField(db_index=True, auto_now=True, null=True)

  def publish(self):
      self.modified_at = timezone.now()
      self.save()

  def __str(self):
      return self.name

class SightseeingSpot(models.Model):
  name = models.CharField(max_length=255, db_index=True)
  key = models.CharField(max_length=255, db_index=True)
  country = models.ForeignKey(Country, on_delete=models.PROTECT, db_index=True)
  created_at = models.DateTimeField(db_index=True, auto_now_add=True, null=True)
  modified_at = models.DateTimeField(db_index=True, auto_now=True, null=True)

  def publish(self):
      self.modified_at = timezone.now()
      self.save()

  def __str(self):
      return self.name

class SightSeeingSpotReview(models.Model):
  name = models.CharField(max_length=255, db_index=True)
  key = models.CharField(max_length=255, db_index=True)
  sightseeingSpot = models.ForeignKey(SightseeingSpot, on_delete=models.PROTECT, db_index=True)
  user = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True)
  created_at = models.DateTimeField(db_index=True, auto_now_add=True, null=True)
  modified_at = models.DateTimeField(db_index=True, auto_now=True, null=True)

  def publish(self):
      self.modified_at = timezone.now()
      self.save()

  def __str(self):
      return self.name
