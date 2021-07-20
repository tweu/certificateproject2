from django.http.response import HttpResponse, HttpResponseRedirect
from onlineshop.forms import ProductForm
from onlineshop.models import Brand, Product
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy

# Create your views here.



class ProductListView(ListView):
    model = Product
    template_name = 'course/product_list.html'
    context_object_name = 'products'
    paginate_by = 3



class ProductDetailView(DetailView):
    model = Product
    template_name = 'course/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'



class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    fields = ['name', 'price', 'photo', 'brand', 'category']
    template_name='course/product_create.html'
    login_url = '/user/login/'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductUpdateNew(LoginRequiredMixin,UpdateView):
    model = Product
    fields = ['name', 'price', 'photo', 'brand', 'category']
    template_name = 'course/product_edit.html'
    pk_url_kwarg = 'product_id'
    login_url = '/user/login/'



class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('product_list')
    login_url = '/user/login/'
