from core.models import Employee

print([(e.first_name, str(e.salary))
      for e in Employee.objects.filter(department__code="IT")])
