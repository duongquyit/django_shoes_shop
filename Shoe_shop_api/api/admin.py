from django.contrib import admin
from . models import Product, Size, Amount, Detail_Bill, Category, User
# Register your models here.
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Amount)
admin.site.register(Detail_Bill)
admin.site.register(Category)
admin.site.register(User)
