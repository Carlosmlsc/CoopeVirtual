from django.conf.urls import url
from .views import product_list, ProductCreate


urlpatterns = [
    url(r'list/$', product_list, name='product_list'),
    url(r'add/$', ProductCreate.as_view(), name='product_create'),

]