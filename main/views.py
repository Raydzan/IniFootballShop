from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    context = {
        'app' : 'inifootballshop',
        'name': 'Moch Raydzan',
        'kelas': 'D',
        "items": Product.objects.all().order_by("-id"),
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_main")
    return render(request, "create_product.html", {"form": form})

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

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