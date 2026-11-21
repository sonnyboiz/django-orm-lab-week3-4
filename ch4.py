from django.db.models import F
from core.models import Product


def purchase(product_id, x):
    updated = Product.objects.filter(pk=product_id, stock_quantity__gte=x).update(
        stock_quantity=F('stock_quantity') - x,
        total_sold=F('total_sold') + x,
        total_revenue=F('total_revenue') + F('price') * x,
    )
    return updated == 1


laptop = Product.objects.get(name="Laptop")

print("Buy 3:", purchase(laptop.pk, 3))
print("Buy 3 again:", purchase(laptop.pk, 3))

p = Product.objects.get(name="Laptop")
print("Stock:", p.stock_quantity, "Sold:",
      p.total_sold, "Revenue:", p.total_revenue)
