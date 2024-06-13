from django.urls import path
from . import views
urlpatterns = [
    #ana sayfa
    path('',views.store, name='store'),
    #ürün
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    #kategori
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    
]