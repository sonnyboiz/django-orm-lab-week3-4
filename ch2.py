from django.db.models import Q, F
from core.models import Product

qs = Product.objects.filter(
    Q(stock_quantity__lte=F('reorder_level')) |
    Q(is_promotional=True, stock_quantity__lt=F('reorder_level') * 2)
)
print([p.name for p in qs])
