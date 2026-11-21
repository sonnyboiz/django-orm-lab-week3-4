from core.models import Product

print([(p.name, str(p.price))
      for p in Product.objects.filter(category__name='Gadgets')])
