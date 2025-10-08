from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.utils import timezone
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
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            # hardening XSS minimal
            p.name = strip_tags(p.name)
            if hasattr(p, "description") and p.description:
                p.description = strip_tags(p.description)
            p.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "product": {
                        "id": str(p.id),
                        "name": p.name,
                        "price": p.price,
                        "stock": p.stock,
                        "description": getattr(p, "description", None),
                        "category": getattr(p, "category", None),
                        "image_url": getattr(p, "image_url", "") or "",
                        "user": (p.user.username if getattr(p, "user_id", None) else None),
                        "created_at": (p.created_at.isoformat() if getattr(p, "created_at", None) else None),
                        "updated_at": (p.updated_at.isoformat() if getattr(p, "updated_at", None) else None),
                    }
                }, status=201)

            messages.success(request, "Produk berhasil ditambahkan.")
            return redirect('main:show_main')
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = ProductForm()
    return render(request, "create_product.html", {"form": form})


@login_required(login_url='main:login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

@login_required(login_url='main:login')
def update_product(request, id):
    p = get_object_or_404(Product, pk=id)
    if p.user != request.user:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"error": "forbidden"}, status=403)
        messages.error(request, "Kamu bukan pemilik produk ini.")
        return redirect('main:show_main')

    form = ProductForm(request.POST or None, instance=p)
    if request.method == "POST":
        if form.is_valid():
            p = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "updated": True,
                    "product": {
                        "id": str(p.id),
                        "name": p.name,
                        "price": p.price,
                        "stock": p.stock,
                        "description": getattr(p, "description", None),
                        "category": getattr(p, "category", None),
                        "image_url": getattr(p, "image_url", "") or "",
                        "user": (p.user.username if getattr(p, "user_id", None) else None),
                        "created_at": (p.created_at.isoformat() if getattr(p, "created_at", None) else None),
                        "updated_at": (p.updated_at.isoformat() if getattr(p, "updated_at", None) else None),
                    }
                })
            messages.success(request, "Produk diperbarui.")
            return redirect('main:show_product', id=p.id)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)

    return render(request, "update_product.html", {"form": form, "product": p})


@login_required(login_url='main:login')
@require_POST
def delete_product(request, id):
    p = get_object_or_404(Product, pk=id)
    if p.user != request.user:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"error": "forbidden"}, status=403)
        messages.error(request, "Kamu bukan pemilik produk ini.")
        return redirect('main:show_main')

    p.delete()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({"deleted": True, "id": str(id)})
    messages.success(request, "Produk dihapus.")
    return redirect('main:show_main')

# Form register

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"registered": True}, status=201)
            messages.success(request, "Akun dibuat. Silakan login.")
            return redirect('main:login')
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            ts = timezone.localtime().strftime('%Y-%m-%d %H:%M:%S')
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                resp = JsonResponse({"logged_in": True})
                resp.set_cookie('last_login', ts) 
                return resp
            resp = redirect('main:show_main')
            resp.set_cookie('last_login', ts)
            return resp
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_user(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        logout(request)
        resp = JsonResponse({"logged_out": True})
        resp.delete_cookie('last_login')
        return resp
    logout(request)
    resp = redirect('main:login')
    resp.delete_cookie('last_login')
    return resp

    # not Main function 
    
def show_xml(request):
    qs = Product.objects.all().order_by("-id")
    return HttpResponse(serializers.serialize("xml", qs), content_type="application/xml")


def show_xml_by_id(request, id):
    p = get_object_or_404(Product, pk=id)
    return HttpResponse(serializers.serialize("xml", [p]), content_type="application/xml")

def show_json(request):
    qs = Product.objects.select_related("user").all().order_by("-id")
    data = [{
        "id": str(p.id),
        "name": p.name,
        "price": p.price,
        "stock": p.stock,
        "description": getattr(p, "description", None),
        "category": getattr(p, "category", None),
        "image_url": getattr(p, "image_url", "") or "",
        "user": (p.user.username if getattr(p, "user_id", None) else None),
        "created_at": (p.created_at.isoformat() if getattr(p, "created_at", None) else None),
        "updated_at": (p.updated_at.isoformat() if getattr(p, "updated_at", None) else None),
    } for p in qs]
    return JsonResponse(data, safe=False)

def show_json_by_id(request, id):
    p = get_object_or_404(Product.objects.select_related("user"), pk=id)
    data = {
        "id": str(p.id),
        "name": p.name,
        "price": p.price,
        "stock": p.stock,
        "description": getattr(p, "description", None),
        "category": getattr(p, "category", None),
        "image_url": getattr(p, "image_url", "") or "",
        "user": (p.user.username if getattr(p, "user_id", None) else None),
        "created_at": (p.created_at.isoformat() if getattr(p, "created_at", None) else None),
        "updated_at": (p.updated_at.isoformat() if getattr(p, "updated_at", None) else None),
    }
    return JsonResponse(data)