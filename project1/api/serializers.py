from dataclasses import fields
from importlib.metadata import files
from pyexpat import model
from rest_framework import serializers
from api.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'description']