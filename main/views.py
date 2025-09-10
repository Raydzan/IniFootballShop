from django.shortcuts import render

def show_main(request):
    context = {
        'price' : '200000',
        'name': 'si bolang',
        'category': 'Bayern kit 24/25'
    }

    return render(request, "main.html", context)