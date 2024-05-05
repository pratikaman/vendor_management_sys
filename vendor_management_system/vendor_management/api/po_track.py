from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins

from ..models import PurchaseOrder
from ..serializers.po_serializer import PurchaseOrderSerializer


class PurchaseOrderList(generics.ListCreateAPIView):
    """
    API endpoint that allows listing all purchase orders or creating a new purchase order.
    """
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class PurchaseOrderDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                          generics.GenericAPIView):
    """
    API endpoint that allows retrieving, updating, or deleting a purchase order.
    """

    lookup_field = 'po_number'
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns the queryset for retrieving a specific purchase order based on the provided 'po_number' parameter.
        """
        po_number = self.kwargs.get('po_number')
        return PurchaseOrder.objects.filter(po_number=po_number)

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to retrieve a specific purchase order.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Handles PUT requests to update a specific purchase order.
        Allows partial updates by setting 'partial' parameter to True.
        """
        kwargs['partial'] = True
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Handles DELETE requests to delete a specific purchase order.
        """
        return self.destroy(request, *args, **kwargs)
