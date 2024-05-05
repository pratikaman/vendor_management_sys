from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from datetime import datetime

from ..models import PurchaseOrder
from ..serializers.po_serializer import PurchaseOrderSerializer


class PurchaseOrderAcknowledgement(APIView):
    """
     Acknowledge a purchase order.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, po_number):
        try:
            return PurchaseOrder.objects.get(po_number=po_number)
        except PurchaseOrder.DoesNotExist:
            raise Http404

    def post(self, request, po_number):
        po = self.get_object(po_number)
        if po.acknowledgment_date:
            return Response({'error': 'PO already acknowledged'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PurchaseOrderSerializer(po, data={'acknowledgment_date': datetime.now()}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
