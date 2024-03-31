from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import generic
from .filters import *


def home(request):
    shops = Shop.objects.filter(is_shop=True)
    return render(request, 'index.html', {'shops': shops})


def shop_detail(request, id):
    shop = get_object_or_404(Shop, id=id)
    products = Product.objects.filter(shop=shop, is_active=True)
    return render(request, 'detail.html', {'shop': shop, 'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'itemDetail.html', {'product': product})


class ProductListView(generic.ListView):
    template_name = 'productlist.html'
    queryset = Product.objects.filter(is_active=True)
    context_object_name = 'products'
    model = Product
    paginate_by = 20
    filter_class = ProductFilter

    def get_queryset(self):
        query = Product.objects.filter(is_active=True)
        filter = ProductFilter(self.request.GET, queryset=query)
        query = filter.qs
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter().form

        return context
