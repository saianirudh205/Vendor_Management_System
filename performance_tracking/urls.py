from django.urls import path
from .views import VendorPerformanceAPIView

urlpatterns = [
    path('api/vendors/<int:pk>/performance/',
         VendorPerformanceAPIView.as_view(), name='vendor-performance'),
]
