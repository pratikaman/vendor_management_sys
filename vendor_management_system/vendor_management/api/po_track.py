from rest_framework import permissions
from rest_framework import generics

from ..models import PurchaseOrder
from ..serializers.po_serializer import PurchaseOrderSerializer


class PurchaseOrderList(generics.ListCreateAPIView):
    """
    List all purchase orders, or create a new purchase order.
    """
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a purchase order.
    """

    lookup_field = 'po_number'
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        po_number = self.kwargs.get('po_number')
        return PurchaseOrder.objects.filter(po_number=po_number)
