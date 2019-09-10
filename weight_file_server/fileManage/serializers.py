from rest_framework import serializers
from .models import *


class ImageFileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = ImageFile
        fields = '__all__'


class WeightFileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = WeightFile
        fields = '__all__'