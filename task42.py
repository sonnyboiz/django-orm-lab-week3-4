from decimal import Decimal
from django.db.models import F
from core.models import Employee

updated = Employee.objects.filter(department__code="IT").update(
    salary=F('salary') * Decimal('1.10'))
print("Rows updated:", updated)

for emp in Employee.objects.filter(department__code="IT"):
    print(emp.first_name, "New Salary:", emp.salary)
