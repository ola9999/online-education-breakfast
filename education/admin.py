from django.contrib import admin
from education.models import (Subject,
							  Lecture,
							  Reference,
							  Course,
							  Favourite_Lecture,
							  Favourite_Course,
							  # C
							  )

# Register your models here.

class Subjectadmin(admin.ModelAdmin):
	list_display = ('subject_name','year','semister')

class Lectureadmin(admin.ModelAdmin):
	list_display = ('id','s_id','lecture_title','lecture_url','typee')

class Referenceadmin(admin.ModelAdmin):
	list_display = ('s_id','reference_name','reference_url')

class Courseadmin(admin.ModelAdmin):
	list_display = ('id','s_id','course_name','course_url','typee')

class Favourite_Lectureadmin(admin.ModelAdmin):
	list_display = ('lec_id',)

class Favourite_Courseadmin(admin.ModelAdmin):
	list_display = ('cor_id',)


# admin.site.register(C)

admin.site.register(Subject,Subjectadmin)
admin.site.register(Lecture,Lectureadmin)

admin.site.register(Reference,Referenceadmin)
admin.site.register(Course,Courseadmin)


admin.site.register(Favourite_Lecture,Favourite_Lectureadmin)
admin.site.register(Favourite_Course,Favourite_Courseadmin)

    