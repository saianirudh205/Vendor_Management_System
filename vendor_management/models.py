# vendor_management/models.py

from django.db import models

'''
● name: CharField - Vendor's name.
● contact_details: TextField - Contact information of the vendor.
● address: TextField - Physical address of the vendor.
● vendor_code: CharField - A unique identifier for the vendor.
● on_time_delivery_rate: FloatField - Tracks the percentage of on-time deliveries.
● quality_rating_avg: FloatField - Average rating of quality based on purchase
orders.
● average_response_time: FloatField - Average time taken to acknowledge
purchase orders.
● fulfillment_rate: FloatField - Percentage of purchase orders fulfilled successfully.

'''


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
