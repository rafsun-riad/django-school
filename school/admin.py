from django.contrib import admin
from school.models import Class, Subject, Student, ClassSubject, Mark

# Register your models here.
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(ClassSubject)
admin.site.register(Mark)
