from django.shortcuts import render

from education.models import Subject,Lecture,Reference,Courses
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def subject_view(request, pk ):

	if request.method == 'GET':
		subjects = Subject.objects.filter(year= pk)	
		sub=[]
		sem=[]
		data={}

		for s in subjects:
			sub.append(s.subject_name)
			sem.append(s.semister)

			
		data={"subject_name":sub,
			  "semister":sem
			  }
		# print(les)
		print()
		print(data)
		return JsonResponse(data)
		

@api_view(['GET'])
def lecture_view(request, pk ):

	if request.method == 'GET':
		lectures = Lecture.objects.filter(s_id= pk)	
		les=[]
		url=[]

		for s in lectures:
			les.append(s.lecture_title)
			url.append(s.lecture_url)

		print(les)
		data ={"lecture_title":les,
			   "lecture_url": url
				}
		return JsonResponse(data)


@api_view(['GET'])
def reference_view(request, pk ):

	if request.method == 'GET':
		reference = Reference.objects.filter(s_id= pk)

		les=[]
		url=[]


		for s in reference:
			les.append(s.reference_name)
			url.append(s.reference_url)


		data ={"reference_name":les,
			   "reference_url": url
		}


		print(les)
		return JsonResponse(data)

@api_view(['GET'])
def course_view(request, pk ):

	if request.method == 'GET':
		reference = Reference.objects.filter(s_id= pk)

		les=[]
		url=[]

		for s in reference:
			les.append(s.course_name)
			url.append(s.course_url)

		print(les)
		data = {"course_name":les,
				"course_url":url
				}
		return JsonResponse(data)

