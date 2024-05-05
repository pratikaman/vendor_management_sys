from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins

from ..models import PurchaseOrder
from ..serializers.po_serializer import PurchaseOrderSerializer


class PurchaseOrderList(generics.ListCreateAPIView):
    """
    List all purchase orders, or create a new purchase order.
    """
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class PurchaseOrderDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                          generics.GenericAPIView):
    """
    Retrieve, update or delete a purchase order.
    """

    lookup_field = 'po_number'
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        po_number = self.kwargs.get('po_number')
        return PurchaseOrder.objects.filter(po_number=po_number)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):

        # Allowing partial updates in PUT request
        kwargs['partial'] = True
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
