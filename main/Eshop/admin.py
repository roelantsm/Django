from django.contrib import admin
from.models import Category
from.models import Product
from.models import Cart
from.models import CartItem
from.models import Order
from.models import Adress


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Adress)