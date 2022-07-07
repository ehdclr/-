from django.shortcuts import render
from .models import Product
from .forms import ProductForm


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()


    form = ProductForm
    return render(request,'stock/index.html', {'form': form})