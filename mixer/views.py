from rest_framework import viewsets

from mixer.models import Mixtape
from mixer.serializers import MixtapSerializer


class MixtapeViewSet(viewsets.ModelViewSet):
	queryset = Mixtape.objects.all()
	serializer_class = MixtapSerializer
