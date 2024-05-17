from rest_framework import serializers
from .models import Poc

class PocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poc
        fields = ["currentTime"]