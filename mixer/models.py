from django.conf import settings
from django.db import models


class Song(models.Model):
	name = models.CharField(max_length=255)
	artist_name = models.CharField(max_length=255)
	position = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name


class Mixtape(models.Model):
	owner = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
		related_name='mixtapes')
	name = models.CharField(max_length=255)
	played_count = models.PositiveIntegerField()
	songs = models.ManyToManyField(Song, related_name='+')
	saved_users = models.ManyToManyField(
		settings.AUTH_USER_MODEL, related_name='saved_mixtapes')

	def __str__(self):
		return self.name
