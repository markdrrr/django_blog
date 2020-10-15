from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('detail/<int:product_pk>', views.product_detail, name='product_detail'),
    path('product_in_basket/', views.product_in_basket, name='product_in_basket')
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)