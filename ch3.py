from decimal import Decimal
from django.db.models import F, Case, When, DecimalField
from core.models import Product

new_price = F('price') * Decimal('1.15')

updated = Product.objects.filter(category__name='Gadgets').update(
    price=Case(
        When(max_allowed_price__lt=new_price, then=F('max_allowed_price')),
        default=new_price,
        output_field=DecimalField(max_digits=10, decimal_places=2),
    )
)
print("Rows updated:", updated)
