from django.urls import path
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("", ProductListView.as_view(), name="product_list")
]
