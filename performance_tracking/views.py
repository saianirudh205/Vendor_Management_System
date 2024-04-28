from rest_framework import generics
from .models import Vendor, HistoricalPerformance
from vendor_management.serializers import VendorSerializer
from .logic import calculate_performance_metrics
from rest_framework.response import Response


class VendorPerformanceAPIView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Calculate and update performance metrics
        res = calculate_performance_metrics(instance)
        if not res:
            return Response([])

        serializer = self.get_serializer(res)
        print(serializer.data)
        return Response(serializer.data)

        return res
        print(
            "data--", [(i.average_response_time, i.date) for i in HistoricalPerformance.objects.all()])
        performance_data = HistoricalPerformance.objects.filter(
            vendor=instance).latest('date')
        print(performance_data)
        serializer = self.get_serializer(instance)
        print(serializer.data)
        return Response(serializer.data)
