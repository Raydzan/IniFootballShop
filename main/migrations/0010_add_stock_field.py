from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
