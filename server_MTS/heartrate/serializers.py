from rest_framework import serializers
from .models import Heartrate

class HeartRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartrate
        fields = ('BPM', 'RESP', 'time')
