import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product

@login_required(login_url='main:login')
def show_main(request):
    f = request.GET.get("filter", "all")
    cat = request.GET.get("category", "").strip()

    qs = Product.objects.all()
    if f == "yours":
        qs = qs.filter(user=request.user)
    if cat:
        qs = qs.filter(category=cat)
    
    items = Product.objects.all().order_by("-created_at")

    context = {
        "items": qs.order_by("-created_at"),
        "active_filter": f,
        "active_category": cat,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

# product function

@login_required(login_url='main:login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect("main:show_main")
    return render(request, "create_product.html", {"form": form})

@login_required(login_url='main:login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if product.user != request.user:
        messages.error(request, "bukan pemilik")
        return redirect("main:show_main")

    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Produk berhasil diperbarui.")
        return redirect("main:show_main")
    return render(request, "update_product.html", {"form": form, "product": product})

@login_required(login_url='main:login')
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if product.user != request.user:
        messages.error(request, "bukan pemilik")
        return redirect("main:show_main")

    if request.method == "POST":
        product.delete()
        messages.success(request, "Produk telah dihapus.")
        return redirect("main:show_main")
    # Halaman konfirmasi
    return render(request, "delete_product.html", {"product": product})

# Form register

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    return render(request, 'register.html', {'form': form})

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

    # not Main function 

def show_xml(request):
    data = Product.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, product_id):
    obj = get_object_or_404(Product, pk=product_id)
    xml_data = serializers.serialize("xml", [obj])
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")

def show_json_by_id(request, product_id):
    obj = get_object_or_404(Product, pk=product_id)
    json_data = serializers.serialize("json", [obj])
    return HttpResponse(json_data, content_type="application/json")