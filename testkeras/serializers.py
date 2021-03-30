from rest_framework import serializers
from .models import Heartrate
import time

class HeartRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartrate
        fields = ('BPM', 'time')
