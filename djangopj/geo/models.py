from django.db import models

from django.utils import timezone

class Country(models.Model):
  name = models.CharField(max_length=255, db_index=True)
  key = models.CharField(max_length=2, db_index=True)
  created_at = models.DateTimeField(default=timezone.now, db_index=True)
  modified_at = models.DateTimeField(blank=True, null=True, db_index=True)

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
  created_at = models.DateTimeField(default=timezone.now, db_index=True)
  modified_at = models.DateTimeField(blank=True, null=True, db_index=True)

  def publish(self):
      self.modified_at = timezone.now()
      self.save()

  def __str(self):
      return self.name
