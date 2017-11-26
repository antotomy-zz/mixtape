from rest_framework import serializers

from mixer.models import Mixtape, Song


class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ('id', 'name', 'artist_name', 'position')


class MixtapSerializer(serializers.ModelSerializer):
	songs = SongSerializer(many=True)

	class Meta:
		model = Mixtape
		fields = ('id', 'name', 'played_count', 'songs')
