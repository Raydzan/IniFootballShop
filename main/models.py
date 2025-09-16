import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Sepatu Bola'),
        ('accessory', 'Aksesoris'),
        ('ball', 'Bola'),
        ('others', 'Lainnya'),
    ]

    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='jersey')
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name