#/Users/samhsu/Desktop/Personal Learning/Python learning/Django-learning/ecommerce/products/templatetags/cart_template_tags.py
from django import template
from ..models import Order, OrderProduct

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)

        if qs.exists():
             return qs[0].totalItems() 
    return 0
