from django.contrib import admin

# Register your models here.
from shop.models import Product
from shop.models import User
from shop.models import Order


admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)