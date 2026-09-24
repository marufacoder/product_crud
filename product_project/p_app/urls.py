from django.contrib import admin
from django.urls import path
from p_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('add_product/', add_product, name='add_product'),
    path('product_list/', product_list, name='product_list'),

       path('delete_product/<str:pro_id>/',delete_product, name='delete_product'),
    path('update_product/<str:pro_id>/',update_product, name='update_product'),
]