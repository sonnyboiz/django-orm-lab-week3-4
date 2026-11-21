from decimal import Decimal
from core.models import Category, Product

elec = Category.objects.create(name="Electronics")
gadg = Category.objects.create(name="Gadgets")

Product.objects.create(name="Laptop", category=elec, price=Decimal("25000"), max_allowed_price=Decimal(
    "30000"), stock_quantity=5, reorder_level=10, status="NORMAL", warehouse_country="Japan")
Product.objects.create(name="Phone", category=elec, price=Decimal("8000"), max_allowed_price=Decimal(
    "9000"), stock_quantity=50, reorder_level=10, status="DISCOUNTED", warehouse_country="China")
Product.objects.create(name="Tablet", category=elec, price=Decimal("12000"), max_allowed_price=Decimal(
    "15000"), stock_quantity=15, reorder_level=10, is_promotional=True, status="DISCOUNTED", warehouse_country="Korea")
Product.objects.create(name="Smart Watch", category=gadg, price=Decimal("1000"), max_allowed_price=Decimal(
    "1100"), stock_quantity=20, reorder_level=10, status="NORMAL", warehouse_country="Thailand")
Product.objects.create(name="Earbuds", category=gadg, price=Decimal("2000"), max_allowed_price=Decimal(
    "2600"), stock_quantity=8, reorder_level=10, status="CLEARANCE", warehouse_country="China")
print("Products created:", Product.objects.count())
