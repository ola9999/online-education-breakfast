from django.contrib import admin
from education.models import Subject,Lecture,Reference,Courses
# Register your models here.


admin.site.register(Subject)
admin.site.register(Lecture)

admin.site.register(Reference)
admin.site.register(Courses)