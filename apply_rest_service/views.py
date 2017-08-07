from django.shortcuts import render

from db_tables.models import Items, Player
from rest_framework import viewsets
from apply_rest_service.serializers import PlayerSerializer, ItemsSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

