import datetime
from django.db.models import Count, Avg
from purchase_order_management.models import PurchaseOrder
from .models import HistoricalPerformance

from django.db.models import Count, Avg, F  # Import F from Django's ORM
from django.utils import timezone


def calculate_performance_metrics(vendor):
    completed_orders = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed')

    print("----", completed_orders)
    # On-Time Delivery Rate
    total_completed_orders = completed_orders.count()
    on_time_delivered_orders = completed_orders.filter(
        delivery_date__lte=F('acknowledgment_date')).count()
    on_time_delivery_rate = (on_time_delivered_orders /
                             total_completed_orders) * 100 if total_completed_orders > 0 else 0

    # Quality Rating Average
    quality_rating_avg = completed_orders.aggregate(
        quality_rating_avg=Avg('quality_rating'))['quality_rating_avg'] or 0

    # Average Response Time
    avg_response_time = completed_orders.aggregate(avg_response_time=Avg(
        F('acknowledgment_date') - F('issue_date')))['avg_response_time'] or 0

    avg_response_time = timedelta_to_float(avg_response_time)
    # Fulfillment Rate
    print("Avg ---", avg_response_time)
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    # Assuming quality rating < 0 indicates issues
    successful_orders = completed_orders.exclude(quality_rating__lt=0).count()
    fulfillment_rate = (successful_orders / total_orders) * \
        100 if total_orders > 0 else 0

    # Save historical performance
    if completed_orders:

        res = HistoricalPerformance.objects.create(
            vendor=vendor,
            date=timezone.now(),
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=avg_response_time,
            fulfillment_rate=fulfillment_rate
        )
        vendor.on_time_delivery_rate = on_time_delivered_orders
        vendor.quality_rating_avg = quality_rating_avg
        vendor.average_response_time = avg_response_time
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()
        return vendor

    return vendor


def timedelta_to_float(timedelta):
    total_hours = timedelta.total_seconds() / 3600  # Convert timedelta to total hours
    days = total_hours // 24
    hours = total_hours % 24
    return days + hours / 24

# Sample input
# timedelta_input = datetime.timedelta(days=1, hours=10, minutes=28, seconds=43, microseconds=612233)

# # Convert and print the result
# result = timedelta_to_float(timedelta_input)
# print(result)  # Output: 1.437532757175926
