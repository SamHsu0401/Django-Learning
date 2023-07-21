#/Users/samhsu/Desktop/Personal Learning/Python learning/Django-learning/ecommerce/products/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    ProductDetailView,
    ProductListView,
    add_to_cart,
    remove_single_product_from_cart,
)

urlpatterns = [
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("add-to-cart/<int:pk>/", add_to_cart, name='add_to_cart'),
    path("remove-from-cart/<int:pk>/", remove_single_product_from_cart, name='remove_from_cart'),
    path("", ProductListView.as_view(), name="products"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)