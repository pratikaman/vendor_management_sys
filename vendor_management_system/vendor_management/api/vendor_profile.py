from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins

from ..models import Vendor
from ..serializers.vendor_serializer import VendorSerializer


class VendorList(generics.ListCreateAPIView):
    """
    API endpoint that allows listing all vendor profiles or creating a new vendor profile.

    """

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]


class VendorDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    """
    API endpoint that allows retrieving, updating, or deleting a vendor profile.

    """

    lookup_field = 'vendor_code'
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns the queryset of Vendor objects filtered by the vendor code.

        """
        vendor_code = self.kwargs.get('vendor_code')
        return Vendor.objects.filter(vendor_code=vendor_code)

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and retrieves a vendor profile.

        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Handles PUT requests and updates a vendor profile.

        """
        # Allowing partial updates in PUT request
        kwargs['partial'] = True
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Handles DELETE requests and deletes a vendor profile.

        """
        return self.destroy(request, *args, **kwargs)
