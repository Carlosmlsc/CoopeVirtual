from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from common.products.models import Product, ProductDepartment, ProductSubDepartment, ProductForSale
from common.companies.models import Company

from django.http import Http404, HttpResponse, HttpResponseServerError, JsonResponse
from django.utils.translation import gettext as _
from django.db import transaction
import json
from django.core.exceptions import ObjectDoesNotExist


class ProductCreate(CreateView):

    model = Product
    template_name = 'products/create.jade'
    success_url = '/products/'

    def get_initial(self):
        super(ProductCreate, self).get_initial()
        company = self.request.user.profile.company_id
        self.initial = {"company": company}
        return self.initial

    fields = ['company', 'code', 'description', 'department', 'subdepartment', 'useinventory',
              'minimum', 'unit', 'cost', ]


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
    fields = ['company', 'code', 'description', 'department', 'subdepartment', 'useinventory',
              'minimum', 'unit', 'cost', ]
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
def product_create(request):

    if request.method == 'GET':

        company = request.user.profile.company_id
        departments = ProductDepartment.objects.filter(company=request.user.profile.company_id)
        subdepartments = ProductSubDepartment.objects.filter(department__company=request.user.profile.company_id)

        return render(request, 'products/create.jade', {'departments': departments, 'subdepartments': subdepartments,
                                                        'company': company})

    if request.method == 'POST':

        data = json.loads(request.body)

        company = request.user.profile.company
        code = data['code']
        unit = data['unit']
        description = data['description']
        department = ProductDepartment.objects.get(pk=data['department'])
        subdepartment = ProductSubDepartment.objects.get(pk=data['subdepartment'])
        cost = data['cost']

        barcode = data['barcode']
        utility = data['utility']
        price = data['price']
        usetaxes = data['useTaxes']
        taxes = data['taxes']
        discount = data['discount']
        sellprice = data['sellprice']

        product = Product(company=company, code=code, unit=unit, description=description, department=department,
                          subdepartment=subdepartment, cost=cost)

        productforsale = ProductForSale(company=company, product=product, code=code, barcode=barcode, description=description,
                                        department=department, subdepartment=subdepartment, unit=unit,
                                        utility=utility, price=price, usetaxes=usetaxes, taxes=taxes,
                                        discount=discount, sellprice=sellprice)
        try:
            with transaction.atomic():

                product.save()

                if data['isForSale']:

                    productforsale.save()

                    return JsonResponse({'product': product.id, 'productforsale': productforsale.id})

                return JsonResponse({'product': product.id, 'productforsale': productforsale.id})

        except Exception as e:
            print e
            return HttpResponseServerError(e)


@login_required
def product_list(request):

    company = request.user.profile.company_id

    products = Product.objects.filter(company=company)

    return render(request, 'products/list.jade', {'products': products})


@login_required
def product_update(request, pk):

    if request.method == 'GET':

        company = request.user.profile.company_id
        departments = ProductDepartment.objects.filter(company=request.user.profile.company_id)
        subdepartments = ProductSubDepartment.objects.filter(department__company=request.user.profile.company_id)

        try:
            product = Product.objects.get(company=request.user.profile.company_id, code=pk)

            if product.hasforsale:
                try:
                    productforsale = ProductForSale.objects.get(company=request.user.profile.company_id, code=pk)
                    return render(request, 'products/update.jade', {'departments': departments,
                                                                    'subdepartments': subdepartments,
                                                                    'company': company, 'product': product,
                                                                    'productforsale': productforsale})
                except Exception as e:
                    return render(request, 'products/update.jade', {'departments': departments,
                                                                    'subdepartments': subdepartments,
                                                                    'company': company, 'product': product,
                                                                    'productforsale': 0})

            return render(request, 'products/update.jade', {'departments': departments,
                                                            'subdepartments': subdepartments,
                                                            'company': company, 'product': product,
                                                            'productforsale': 0})

        except Product.DoesNotExist:
            raise Http404("Producto no encontrado")

    if request.method == 'POST':

        data = json.loads(request.body)

        company = request.user.profile.company
        code = data['code']
        unit = data['unit']
        description = data['description']
        department = ProductDepartment.objects.get(pk=data['department'])
        subdepartment = ProductSubDepartment.objects.get(pk=data['subdepartment'])
        cost = data['cost']

        barcode = data['barcode']
        utility = data['utility']
        price = data['price']
        usetaxes = data['useTaxes']
        taxes = data['taxes']
        discount = data['discount']
        sellprice = data['sellprice']

        product = Product.objects.get(company=request.user.profile.company_id, code=pk)

        product.company = company
        product.code = code
        product.unit = unit
        product.description = description
        product.department = department
        product.subdepartment = subdepartment
        product.cost = cost

        if data['isForSale']:

            try:

                productforsale = ProductForSale.objects.get(company=request.user.profile.company_id, code=pk)

                productforsale.company = company
                productforsale.product = product
                productforsale.code = code
                productforsale.barcode = barcode
                productforsale.description = description
                productforsale.department = department
                productforsale.subdepartment = subdepartment
                productforsale.unit = unit
                productforsale.utility = utility
                productforsale.price = price
                productforsale.usetaxes = usetaxes
                productforsale.taxes = taxes
                productforsale.discount = discount
                productforsale.sellprice = sellprice

            except ObjectDoesNotExist:

                productforsale = ProductForSale(company=company, product=product, code=code, barcode=barcode,
                                                description=description,
                                                department=department, subdepartment=subdepartment, unit=unit,
                                                utility=utility, price=price, usetaxes=usetaxes, taxes=taxes,
                                                discount=discount, sellprice=sellprice)
            try:
                with transaction.atomic():

                    product.save()

                    if data['isForSale']:

                        productforsale.save()

                        return JsonResponse({'product': product.id, 'productforsale': productforsale.id})

                    return JsonResponse({'product': product.id, 'productforsale': productforsale.id})

            except Exception as e:
                print e
                return HttpResponseServerError(e)

        else:
            try:
                with transaction.atomic():

                    product.save()

                    return JsonResponse({'product': product.id, 'productforsale': ''})

            except Exception as e:
                print e
                return HttpResponseServerError(e)
