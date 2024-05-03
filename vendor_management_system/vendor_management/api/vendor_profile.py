from rest_framework import permissions
from rest_framework import generics

from ..models import Vendor
from ..serializers.vendor_serializer import VendorSerializer
from ..serializers.performance_serializer import HistoricalPerformanceSerializer


class VendorList(generics.ListCreateAPIView):
    """
    List all vendor profiles, or create a new vendor profile.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a vendor profile.
    """

    lookup_field = 'vendor_code'
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        vendor_code = self.kwargs.get('vendor_code')
        return Vendor.objects.filter(vendor_code=vendor_code)


class VendorPerformance(generics.ListAPIView):
    """
    Retrieve historical performance of a vendor.
    """

    serializer_class = HistoricalPerformanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        vendor_code = self.kwargs.get('vendor_code')
        return Vendor.objects.filter(vendor_code=vendor_code)
