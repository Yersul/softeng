from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Timee
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response


class TimeView(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet,):
    queryset = Timee.objects.all()
    permission_classes = [AllowAny,]
    serializer_class =

    def get(self, request):
        obj = Timee.objects.all()
        return Response({
            'posts': obj
        })
