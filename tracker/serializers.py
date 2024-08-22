from rest_framework import serializers
from .models import TrackingNumber

class TrackingNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingNumber
        fields = ['number', 'created_at']
