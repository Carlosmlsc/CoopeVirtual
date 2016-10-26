from django.views.generic.edit import CreateView
from common.products.models import Product


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/create.jade'
    fields = ['code', 'barcode', 'description', 'department', 'subdepartment', 'useinventory', 'inventory',
              'minimum', 'sellmethod', 'cost', 'autoprice', 'utility','price', 'usetaxes', 'taxes', 'discount',
              'sellprice']
