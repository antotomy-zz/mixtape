from django.contrib import admin

from mixer.models import Mixtape, Song


class SongInline(admin.StackedInline):
	model = Song
	extra = 2

class MixtapeAdmin(admin.ModelAdmin):
	inlines = [SongInline]

admin.site.register(Mixtape, MixtapeAdmin)
