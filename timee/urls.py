from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from timee.views import TimeViewSet

router = DefaultRouter()

router.register('', TimeViewSet)

urlpatterns = [
    path('<int>id/', TimeViewSet.as_view({'put': 'retrieve'})),
] + router.urls
