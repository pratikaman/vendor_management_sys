from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from datetime import datetime, timedelta

from .models import PurchaseOrder, HistoricalPerformance


@receiver(post_save, sender=PurchaseOrder)
def on_time_delivery_rate(sender, instance, created, **kwargs):
    """
    Signal to calculate and update the on-time delivery rate for a vendor when a PurchaseOrder is saved.

    """
    if instance.tracker.has_changed('status') and instance.status == 'completed':
        vendor = instance.vendor

        completed_purchase_orders = vendor.purchaseorder_set.filter(status='completed')

        on_time_deliveries = completed_purchase_orders.filter(delivery_date__gte=F('completion_date')).count()
        total_deliveries = completed_purchase_orders.count()

        vendor.on_time_delivery_rate = on_time_deliveries / total_deliveries
        vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def quality_rating_avg(sender, instance, created, **kwargs):
    """
    Signal to calculate and update the average quality rating for a vendor when a PurchaseOrder is saved.

    """
    if instance.tracker.has_changed('status') and instance.status == 'completed':
        vendor = instance.vendor

        completed_purchase_orders = vendor.purchaseorder_set.filter(status='completed')

        quality_ratings_avg = completed_purchase_orders.aggregate(Avg('quality_rating', default=0))

        vendor.quality_rating_avg = quality_ratings_avg['quality_rating__avg']
        vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def average_response_time(sender, instance, created, **kwargs):
    """
    Signal to calculate and update the average response time for a vendor when a PurchaseOrder is saved.

    """
    if instance.tracker.has_changed('acknowledgment_date') and instance.acknowledgment_date is not None:
        vendor = instance.vendor

        acknowledged_purchase_orders = vendor.purchaseorder_set.filter(acknowledgment_date__isnull=False)

        response_times = acknowledged_purchase_orders.annotate(
            response_time=F('acknowledgment_date') - F('order_date'))

        avg_response_time = response_times.aggregate(Avg('response_time'))

        vendor.average_response_time = avg_response_time['response_time__avg'].total_seconds()
        vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def fulfilment_rate(sender, instance, created, **kwargs):
    """
    Signal to calculate and update the fulfilment rate for a vendor when a PurchaseOrder is saved.

    """
    if instance.tracker.has_changed('status'):
        vendor = instance.vendor

        completed_purchase_orders = vendor.purchaseorder_set.filter(status='completed').count()
        total_purchase_orders = vendor.purchaseorder_set.count()

        vendor.fulfillment_rate = completed_purchase_orders / total_purchase_orders if total_purchase_orders > 0 else 0
        vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def create_historical_performance(sender, instance, created, **kwargs):
    """
    Signal to create a HistoricalPerformance record for a vendor when a PurchaseOrder is changed.

    """
    if instance.tracker.changed():
        vendor = instance.vendor

        HistoricalPerformance.objects.create(
            vendor=vendor,
            date=datetime.now(),
            on_time_delivery_rate=vendor.on_time_delivery_rate,
            quality_rating_avg=vendor.quality_rating_avg,
            average_response_time=vendor.average_response_time,
            fulfillment_rate=vendor.fulfillment_rate,
        )
