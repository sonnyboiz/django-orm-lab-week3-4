from django.db.models import Q
from core.models import Employee

# Query 1: IT department OR salary above 70000
qs1 = Employee.objects.filter(Q(department__code="IT") | Q(salary__gt=70000))
print("OR results:", list(qs1))
print("SQL:", qs1.query)

# Query 2: first name contains John AND NOT in HR
qs2 = Employee.objects.filter(
    Q(first_name__icontains="John") & ~Q(department__code="HR"))
print("AND NOT results:", list(qs2))
print("SQL:", qs2.query)
