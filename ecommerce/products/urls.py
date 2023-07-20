from django.urls import path
from .views import(
    ProductDetailView, 
    ProductListView,
    add_to_cart,
    remove_from_cart
    
    )

urlpatterns = [
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("add-to-cart/<int:pk>/", add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove-from-cart'),
    path("", ProductListView.as_view(), name="product_list")
]
