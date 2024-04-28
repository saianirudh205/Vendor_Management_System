# vendor_management/urls.py

from django.urls import path
from .views import VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/vendors/', VendorListCreateAPIView.as_view(), name='vendor-list'),
    path('api/vendors/<int:pk>/',
         VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-detail'),
]
