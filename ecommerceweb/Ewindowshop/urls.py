from django.urls import path

from . import views

urlpatterns = [

   #Shop main page
    path('',views.ecommercesite,name='ecommercesite'),
    
    #Indivisual product
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    
    
    #Indivisual category
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
]