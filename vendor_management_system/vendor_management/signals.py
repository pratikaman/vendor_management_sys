from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

from .models import PurchaseOrder


@receiver(post_save, sender=PurchaseOrder)
def on_time_delivery_rate(sender, instance, created, **kwargs):
    if instance.tracker.has_changed('status') and instance.status == 'completed':
        #
        vendor = instance.vendor

        completed_purchase_orders = vendor.purchaseorder_set.filter(status='completed')

        on_time_deliveries = completed_purchase_orders.filter(delivery_date__gte=F('completion_date')).count()
        total_deliveries = completed_purchase_orders.count()

        vendor.on_time_delivery_rate = on_time_deliveries / total_deliveries
        vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def quality_rating_avg(sender, instance, created, **kwargs):
    if instance.tracker.has_changed('status') and instance.status == 'completed':
        vendor = instance.vendor

        completed_purchase_orders = vendor.purchaseorder_set.filter(status='completed')

        quality_ratings_avg = completed_purchase_orders.aggregate(Avg('quality_rating', default=0))

        vendor.quality_rating_avg = quality_ratings_avg['quality_rating__avg']
        vendor.save()

# @receiver(post_save, sender=PurchaseOrder)
# def average_response_time(sender, instance, created, **kwargs):
#     if instance.tracker.has_changed('acknowledgment_date') and instance.acknowledgment_date:
#         vendor = instance.vendor
#
#         completed_purchase_orders = vendor.purchaseorder_set.filter(status='completed')
#
#         response_times = completed_purchase_orders.filter(acknowledgment_date__isnull=False).annotate(
#             response_time=F('acknowledgment_date') - F('order_date'))
#
#         avg_response_time = response_times.aggregate(Avg('response_time', default=0))
#
#         vendor.average_response_time = avg_response_time['response_time__avg']
#         vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def fulfilment_rate(sender, instance, created, **kwargs):
    if instance.tracker.changed():

        vendor = instance.vendor

        completed_purchase_orders = vendor.purchaseorder_set.filter(status='completed').count()
        total_purchase_orders = vendor.purchaseorder_set.count()

        vendor.fulfillment_rate = completed_purchase_orders / total_purchase_orders
        vendor.save()
