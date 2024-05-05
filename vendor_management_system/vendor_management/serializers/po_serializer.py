from rest_framework import serializers
from ..models import *


class PurchaseOrderSerializer(serializers.ModelSerializer):
    """
    Serializer class for the PurchaseOrder model.

    """

    class Meta:
        model = PurchaseOrder
        fields = [
            'id',
            'po_number',
            'vendor',
            'order_date',
            'delivery_date',
            'items',
            'quantity',
            'status',
            'quality_rating',
            'issue_date',
            'acknowledgment_date',
            'completion_date',
        ]
        read_only_fields = ['completion_date']
