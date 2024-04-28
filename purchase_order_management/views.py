# purchase_order_management/views.py

from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PurchaseOrder
from django.utils import timezone


class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'po_number'


class PurchaseOrderAcknowledgeView(APIView):
    def post(self, request, po_number):
        purchase_order = get_object_or_404(PurchaseOrder, po_number=po_number)
        # Assuming acknowledgment is done at the current time
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        return Response(status=status.HTTP_200_OK)
