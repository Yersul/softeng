from datetime import date

from django.shortcuts import render

# Create your views here.
from django.views.generic import UpdateView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Timee
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from .permissions import PostOwnerOrReadOnly
from .serializers import TimeSerializer, TimeCreateSerializer, TimeUpdateSerializer


class TimeViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet,):
    queryset = Timee.objects.all()

    permission_classes = [IsAuthenticated,]
    serializer_class = TimeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        serializer_class = TimeSerializer

        if self.action == 'create':
            serializer_class = TimeCreateSerializer
        if self.action == 'update':
            serializer_class = TimeUpdateSerializer
        return serializer_class

    def get_permissions(self):
        permission_classes = [IsAuthenticated, ]

        if self.action == 'retrieve' or self.action == 'create' or self.action == 'update' or \
                self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated, PostOwnerOrReadOnly]

        return [permission() for permission in permission_classes]

    def get(self, request):
        queryset = self.get_queryset()
        serializer = TimeSerializer(queryset, many=True)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     instance = serializer.save()
    #     serializer_data = TimeCreateSerializer(instance).data
    #     return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     instance = serializer.save()
    #     serializer_data = TimeUpdateSerializer(instance).data
    #     return Response(data=serializer_data, status=status.HTTP_202_ACCEPTED)

# class BlogModerateViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet, ):
#     permission_classes = [IsAuthenticated, ]
#     serializer_class = TimeSerializer
#     queryset = Timee.objects.all()
#
#
#     def get_serializer_class(self):
#         serializer_class = TimeSerializer
#
#         if self.action == 'create':
#             serializer_class = TimeCreateSerializer
#         if self.action == 'update':
#             serializer_class = TimeUpdateSerializer
#         return serializer_class
#
#     def get_permissions(self):
#         permission_classes = [IsAuthenticated, ]
#
#         if self.action == 'retrieve':
#             permission_classes = [IsAuthenticated, PostOwnerOrReadOnly]
#         elif self.action == 'update' or self.action == 'partial_update':
#             permission_classes.append(PostOwnerOrReadOnly)
#
#         return [permission() for permission in permission_classes]
#
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

