from django.urls import path
from . import views

urlpatterns = [
    path("cart/add/", views.add_to_cart),
    path("cart/view/<uuid:cart_id>/", views.view_cart),
    path("checkout/", views.checkout),
    path("admin/generate-discount/", views.generate_discount),
    path("admin/analytics/", views.analytics),
]
