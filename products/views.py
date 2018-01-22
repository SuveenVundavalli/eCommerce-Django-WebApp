from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Product
from django.http import Http404


# Create your views here.
class ProductFeaturedListView(ListView):
    template_name = "products/product_list.html"
    queryset = Product.objects.featured()

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


# Create your views here.
class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/product_featured_detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductListView(ListView):
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance
