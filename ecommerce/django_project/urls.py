#/Users/samhsu/Desktop/Personal Learning/Python learning/Django-learning/ecommerce/django_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("products/", include("products.urls")),
    path("", include("pages.urls"))
]
