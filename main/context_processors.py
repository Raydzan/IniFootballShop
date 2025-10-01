from .models import Product

def author_info(request):
    return {
        # Navbar kanan identitas
        "navbar_name": "Moch Raydzan",
        "navbar_npm": "2406432482",
        "navbar_kelas": "D",

        # ambil dari models.py
        "product_categories": Product.CATEGORY_CHOICES,
    }