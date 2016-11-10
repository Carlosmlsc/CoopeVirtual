from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from common.products.models import Product

from django.http import Http404
from django.utils.translation import gettext as _


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/create.jade'
    success_url = '/products/'

    def get_initial(self):
        super(ProductCreate, self).get_initial()
        company = self.request.user.profile.company_id
        self.initial = {"company": company}
        return self.initial

    fields = ['company', 'code', 'barcode', 'description', 'department', 'subdepartment', 'useinventory', 'inventory',
              'minimum', 'unit', 'cost', 'autoprice', 'utility', 'price', 'usetaxes', 'taxes', 'discount',
              'sellprice']


class ProductUpdate(UpdateView):

    model = Product

    def get_object(self, queryset=None):

        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        company = self.request.user.profile.company_id

        if pk is not None:
            queryset = queryset.filter(company=company, code=pk)

        else:
            raise AttributeError(u"Generic detail view %s must be called with "
                                 u"either an object pk or a slug."
                                 % self.__class__.__name__)
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj

    template_name = 'products/create.jade'
    fields = ['company', 'code', 'barcode', 'description', 'department', 'subdepartment', 'useinventory', 'inventory',
              'minimum', 'unit', 'cost', 'autoprice', 'utility', 'price', 'usetaxes', 'taxes', 'discount',
              'sellprice']
    success_url = '/products/'


class ProductDelete(DeleteView):

    model = Product

    def get_object(self, queryset=None):

        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        company = self.request.user.profile.company_id

        if pk is not None:
            queryset = queryset.filter(company=company, code=pk)

        else:
            raise AttributeError(u"Generic detail view %s must be called with "
                                 u"either an object pk or a slug."
                                 % self.__class__.__name__)
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj

    success_url = '/products/'
    template_name = 'products/delete.jade'


@login_required
def product_list(request):

    company = request.user.profile.company_id

    products = Product.objects.filter(company=company)

    return render(request, 'products/list.jade', {'products': products})
