from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins

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


class VendorDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    """
    Retrieve, update or delete a vendor profile.
    """

    lookup_field = 'vendor_code'
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        vendor_code = self.kwargs.get('vendor_code')
        return Vendor.objects.filter(vendor_code=vendor_code)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Allowing partial updates in PUT request
        kwargs['partial'] = True
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
