from rest_framework import permissions
from rest_framework import generics

from ..models import Vendor
from ..serializers.vendor_serializer import VendorPerformanceSerializer


class VendorPerformance(generics.ListAPIView):
    """
    API endpoint for listing the performance metrics of a vendor.

    This API endpoint allows authenticated users to retrieve the performance metrics of a specific vendor.
    The performance metrics are returned as a list of serialized vendor objects.

    """

    lookup_field = 'vendor_code'
    serializer_class = VendorPerformanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Get the queryset of vendor objects filtered by the vendor code.

        Returns:
            QuerySet: The queryset of vendor objects filtered by the vendor code.
        """
        vendor_code = self.kwargs.get('vendor_code')
        return Vendor.objects.filter(vendor_code=vendor_code)
