from django.db.models import Q
from core.models import Product

qs = Product.objects.filter(
    Q(category__name='Electronics', price__gt=10000) |
    (Q(status='DISCOUNTED') & ~Q(warehouse_country='China'))
)
print([p.name for p in qs])
