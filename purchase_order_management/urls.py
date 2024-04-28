# purchase_order_management/urls.py

from django.urls import path
from .views import PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView, PurchaseOrderAcknowledgeView

urlpatterns = [
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(),
         name='purchaseorder-list'),
    path('api/purchase_orders/<str:po_number>/',
         PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchaseorder-detail'),
    path('api/purchase_orders/<str:po_number>/acknowledge/',
         PurchaseOrderAcknowledgeView.as_view(), name='acknowledge_purchase_order'),
]
