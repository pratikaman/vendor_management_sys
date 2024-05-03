from django.urls import path
from .views import *
from .api.vendor_profile import VendorList, VendorDetail, VendorPerformance
from .api.po_track import PurchaseOrderList, PurchaseOrderDetail

urlpatterns = [
    path('', home),
    path('vendors/', VendorList.as_view()),
    path('vendors/<str:vendor_code>/', VendorDetail.as_view()),

    path('purchase_orders/', PurchaseOrderList.as_view()),
    path('purchase_orders/<str:po_number>/', PurchaseOrderDetail.as_view()),

    path('vendors/<str:vendor_code>/performance/', VendorPerformance.as_view())
]