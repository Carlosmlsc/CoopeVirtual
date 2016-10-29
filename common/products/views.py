from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from common.products.models import Product


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/create.jade'
    fields = ['code', 'barcode', 'description', 'department', 'subdepartment', 'useinventory', 'inventory',
              'minimum', 'sellmethod', 'cost', 'autoprice', 'utility','price', 'usetaxes', 'taxes', 'discount',
              'sellprice']


@login_required
def product_list(request):

    company = request.user.profile.company_id

    products = Product.objects.filter(company=company)

    return render(request, 'products/list.jade', {'products': products})
