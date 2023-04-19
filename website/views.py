from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import Product


# homepage view
def myhome(request):
    return render(request, 'homepage.html', {'user': request.user})

# cart view
def mycart(request):
    return render(request, 'cart.html')
                  
#product view
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'