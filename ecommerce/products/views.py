from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Product, OrderProduct, Order
from django.shortcuts import redirect
from django.utils import timezone


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
    
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order product is in the order
        if order.products.filter(product__pk = product.pk).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, "This product quantity was updated.")
            return redirect("product_detail", pk=pk)
        else:
            order.products.add(order_product)
            messages.info(request, "This product was added to your cart.")
            return redirect("product_detail", pk=pk)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
        messages.info(request, "This product was added to your cart.")
        return redirect("product_detail", pk=pk)
    
def remove_single_product_from_cart(request, pk):
    product = get_object_or_404(product, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order product is in the order
        if order.products.filter(product__pk=product.pk).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()
            else:
                order.items.remove(order_product)
            messages.info(request, "This item quantity was updated.")
            return redirect("product_detail", pk=pk)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product_detail", pk=pk)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product_detail", pk=pk)
        
            
            
            



