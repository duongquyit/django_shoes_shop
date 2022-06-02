from datetime import datetime
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100, null=True, unique=True)
    password = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name + self.username + self.password

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)
    create_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, null=False)
    product_price = models.FloatField(null=False)
    product_description = models.CharField(max_length=200)
    product_image = models.CharField(max_length=1000, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    create_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.product_name

class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_name = models.CharField(null=False, max_length=20)

    def __str__(self):
        return self.size_name

class Amount(models.Model):
    amount_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}, {}'.format(self.product, self.size, self.quantity)

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=False)
    status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return 'id:{}, user:{}, product:{}, size:{}, quantity:{}'.format(self.cart_id, self.user, self.product, self.size, self.quantity)

class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False, null=True)
    total = models.IntegerField(null=True)
    create_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return 'Id: {}, user: {}, status: {}, total: {}'.format(self.bill_id, self.user, self.status, self.total)

class Bill_Detail(models.Model):
    bill_detais_id = models.AutoField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return 'ID: {}'.format(self.bill_detais_id)