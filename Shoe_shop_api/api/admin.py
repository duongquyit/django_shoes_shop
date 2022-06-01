from django.contrib import admin
from . models import Product, Size, Amount, Bill, Category, User, Cart, Bill_Detail
# Register your models here.
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Amount)
admin.site.register(Bill)
admin.site.register(Bill_Detail)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Cart)

