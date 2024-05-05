from django.contrib import admin
from .models import *
from rest_framework.authtoken.admin import TokenAdmin


# Register your models here.


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_code']
    search_fields = ['vendor_code', 'name']
    readonly_fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['po_number']
    search_fields = ['po_number', 'vendor__vendor_code', 'vendor__name']
    readonly_fields = ['completion_date', 'acknowledgment_date']


@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'date']
    search_fields = ['vendor__vendor_code', 'vendor__name']
    readonly_fields = [
        'vendor',
        'date',
        'on_time_delivery_rate',
        'quality_rating_avg',
        'average_response_time',
        'fulfillment_rate',
    ]


TokenAdmin.raw_id_fields = ['user']