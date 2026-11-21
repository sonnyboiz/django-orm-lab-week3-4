from django.db import connection, reset_queries
from core.models import Employee, Course

reset_queries()
a = [(e.first_name, e.department.name) for e in Employee.objects.all()]
print("Queries (unoptimized):", len(connection.queries))

reset_queries()
b = [(e.first_name, e.department.name)
     for e in Employee.objects.select_related('department').all()]
print("Queries (select_related):", len(connection.queries))

reset_queries()
c = [(x.code, [e.first_name for e in x.attendees.all()])
     for x in Course.objects.prefetch_related('attendees').all()]
print("Queries (prefetch_related):", len(connection.queries))
