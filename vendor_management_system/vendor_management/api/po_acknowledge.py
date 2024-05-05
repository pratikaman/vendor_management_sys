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
    API endpoint to acknowledge a purchase order.

    This API allows authenticated users to acknowledge a purchase order by providing the purchase order number.
    If the purchase order has already been acknowledged, an error message will be returned.
    The acknowledgment date will be set to the current date and time.

    Methods:
    - get_object(po_number): Retrieves the purchase order object based on the provided purchase order number.
    - post(request, po_number): Handles the POST request to acknowledge a purchase order.

    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, po_number):
        """
        Retrieves the purchase order object based on the provided purchase order number.

        Args:
        - po_number (str): The purchase order number.

        Returns:
        - PurchaseOrder: The purchase order object.

        Raises:
        - Http404: If the purchase order with the provided number does not exist.

        """
        try:
            return PurchaseOrder.objects.get(po_number=po_number)
        except PurchaseOrder.DoesNotExist:
            raise Http404

    def post(self, request, po_number):
        """
        Handles the POST request to acknowledge a purchase order.

        Args:
        - request (HttpRequest): The HTTP request object.
        - po_number (str): The purchase order number.

        Returns:
        - Response: The HTTP response containing the acknowledgment data or error message.

        """
        po = self.get_object(po_number)
        if po.acknowledgment_date:
            return Response({'error': 'PO already acknowledged'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PurchaseOrderSerializer(po, data={'acknowledgment_date': datetime.now()}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
