from rest_framework import permissions
from rest_framework import generics

from ..models import Vendor
from ..serializers.vendor_serializer import VendorPerformanceSerializer


class VendorPerformance(generics.ListAPIView):
    """
    List all vendor performance.
    """

    lookup_field = 'vendor_code'
    serializer_class = VendorPerformanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        vendor_code = self.kwargs.get('vendor_code')
        return Vendor.objects.filter(vendor_code=vendor_code)
