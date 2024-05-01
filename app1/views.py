from django.shortcuts import render
from .form import *
from .models import *
# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def contactpage(request):
    return render(request, 'contact.html')

def servicespage(request):
    return render(request, 'services.html')

def basepage(request):
    return render(request, 'base.html')

def pf_fun(request):
    context = {
        'product_form' : Product_form()
    }
    if request.method=="POST":
        product_form = Product_form(request.POST)
        if product_form.is_valid():
            product_form.save()
    return render(request, 'product_add.html', context)