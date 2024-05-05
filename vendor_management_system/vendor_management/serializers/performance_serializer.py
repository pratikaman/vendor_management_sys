from rest_framework import serializers

from .vendor_serializer import VendorSerializer
from ..models import *


class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()
    on_time_delivery_rate = serializers.DecimalField(decimal_places=2, max_digits=5, read_only=True)
    quality_rating_avg = serializers.DecimalField(decimal_places=2, max_digits=5, read_only=True)
    average_response_time = serializers.DecimalField(decimal_places=None, max_digits=None, read_only=True)
    fulfillment_rate = serializers.DecimalField(decimal_places=2, max_digits=5, read_only=True)

    class Meta:
        model = HistoricalPerformance
        read_only_fields = [
            'vendor',
            'date',
            'on_time_delivery_rate',
            'quality_rating_avg',
            'average_response_time',
            'fulfillment_rate',
        ]
