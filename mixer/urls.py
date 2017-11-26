from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from mixer import views


router = DefaultRouter()
router.register(r'mixtapes', views.MixtapeViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
