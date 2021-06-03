
from django.urls import path
from mobile.views import index,add_brand,list_brand,delete_brand,update_brand,create_product,list_products

urlpatterns = [
              path('',index,name='home'),
              path('brands',add_brand,name="add"),
              path('list',list_brand,name = "list"),
              path('delete/<int:id>',delete_brand,name="delete"),
              path('update/<int:id>',update_brand,name = "update"),
              path('products',create_product,name="create"),
              path('items',list_products,name="fetchitems")


]