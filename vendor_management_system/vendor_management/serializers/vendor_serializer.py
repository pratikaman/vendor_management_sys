from rest_framework import serializers
from ..models import *


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = [
            'name',
            'contact_details',
            'address',
            'vendor_code',
        ]


class VendorPerformanceSerializer(serializers.ModelSerializer):
    on_time_delivery_rate = serializers.DecimalField(decimal_places=2, max_digits=5, read_only=True)
    quality_rating_avg = serializers.DecimalField(decimal_places=2, max_digits=5, read_only=True)
    average_response_time = serializers.DecimalField(decimal_places=2, max_digits=5, read_only=True)
    fulfillment_rate = serializers.DecimalField(decimal_places=2, max_digits=5, read_only=True)

    class Meta:
        model = Vendor
        fields = [
            'name',
            'vendor_code',
            'on_time_delivery_rate',
            'quality_rating_avg',
            'average_response_time',
            'fulfillment_rate'
        ]
