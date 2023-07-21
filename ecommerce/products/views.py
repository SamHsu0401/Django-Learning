from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.contrib import messages
from .models import Product, OrderProduct, Order
from django.utils import timezone
from django.views import View


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user = request.user
    
    order_product, created = OrderProduct.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk=product.pk).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, "This product quantity was updated.")
        else:
            order.products.add(order_product)
            messages.info(request, "This product was added to your cart.")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user,
            ordered_date=ordered_date
        )
        order.products.add(order_product)
        messages.info(request, "This product was added to your cart.")
    
    return redirect("product_detail", pk=pk)


def remove_single_product_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk=product.pk).exists():
            order_product = OrderProduct.objects.get(
                product=product,
                user=request.user,
                ordered=False
            )
            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()
            else:
                order.products.remove(order_product)
            messages.info(request, "This item quantity was updated.")
        else:
            messages.info(request, "This item was not in your cart")
    else:
        messages.info(request, "You do not have an active order")
    
    return redirect("product_detail", pk=pk)


class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )




