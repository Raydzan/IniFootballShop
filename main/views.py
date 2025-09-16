from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'inifootballshop',
        'name': 'Moch Raydzan',
        'kelas': 'D'
    }

    return render(request, "main.html", context)
