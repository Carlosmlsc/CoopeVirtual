from django.conf.urls import url
from .views import product_list, ProductCreate, ProductUpdate, ProductDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'list/$', product_list, name='product_list'),
    url(r'add/$', login_required(ProductCreate.as_view()), name='product_create'),
    url(r'update/(?P<pk>[\w-]+)/$', login_required(ProductUpdate.as_view()), name='product_update'),
    url(r'delete/(?P<pk>[\w-]+)/$', login_required(ProductDelete.as_view()), name='product_delete'),

]