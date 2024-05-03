from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_code']
    search_fields = ['vendor_code', 'name']


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['po_number']
    search_fields = ['po_number', 'vendor__vendor_code', 'vendor__name']


@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ['vendor']
    search_fields = ['vendor__vendor_code', 'vendor__name']
