from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('detail/<int:product_pk>', views.product_detail, name='product_detail.html')
]
