from django.urls import path

from .api.po_acknowledge import PurchaseOrderAcknowledgement
from .api.vendor_profile import VendorList, VendorDetail
from .api.po_track import PurchaseOrderList, PurchaseOrderDetail
from .api.vendor_performance import VendorPerformance
from rest_framework.authtoken import views

urlpatterns = [
    path('vendors/', VendorList.as_view()),
    path('vendors/<str:vendor_code>/', VendorDetail.as_view()),
    path('vendors/<str:vendor_code>/performance/', VendorPerformance.as_view()),

    path('purchase_orders/', PurchaseOrderList.as_view()),
    path('purchase_orders/<str:po_number>/', PurchaseOrderDetail.as_view()),
    path('purchase_orders/<str:po_number>/acknowledge', PurchaseOrderAcknowledgement.as_view()),

]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
