from django.db import models
from django.contrib.auth.models import User
from store.models import Product
class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=150)
    address1=models.CharField(max_length=300)
    address2=models.CharField(max_length=300)
    city=models.CharField(max_length=100)

    #opsiyonel
    state=models.CharField(max_length=80, null=True, blank=True)
    zipcode=models.CharField(max_length=30, null=True, blank=True)

    #foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Shipping Address'

    def __str__(self):
        return 'Kargolama Adresi - ' + str(self.id)
class Order(models.Model):
    full_name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    shipping_address=models.TextField(max_length=400)
    amount_paid=models.DecimalField(max_digits=11,decimal_places=2)
    date_ordered=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return 'Sipariş - #' + str(self.id)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity=models.PositiveBigIntegerField(default=1)
    price= models.DecimalField(max_digits=11, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return 'Sipariş İçeriği - #' + str(self.id)
