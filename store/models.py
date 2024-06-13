from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=75, db_index=True)
    slug = models.SlugField(max_length=75, unique=True)

    class Meta:
        verbose_name_plural ='categories'
#category ve productun numarası yerine adının görünmesi için yazılan fonksiyon
    def __str__(self):
       return self.name   
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])  

class Product(models.Model):
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=75)
    #brand girilmezse otomatik olarak un-branded olarak geliyor
    brand=models.CharField(max_length=75, default='un-branded')
    description=models.TextField(blank=True)
    slug =models.SlugField(max_length=75)
    price=models.DecimalField(max_digits=11, decimal_places=2) 
    image=models.ImageField(upload_to='images/') 

    class Meta:
        verbose_name_plural ='products'

    def __str__(self):
       return self.title   
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug]) 
