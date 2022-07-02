from dataclasses import fields
from django.urls import path 
from .models import Link

from rest_framework import serializers


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
