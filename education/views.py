from django.shortcuts import render

from education.models import Subject,Lecture,Reference,Course,Favourite_Lecture,Favourite_Course
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def subject_view(request, id ):

	if request.method == 'GET':
		subjects = Subject.objects.filter(year= id)	
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
def lecture_view(request, id ):

	if request.method == 'GET':
		lectures = Lecture.objects.filter(s_id= id)	
		les=[]
		url=[]
		ids=[]
		types=[]

		for s in lectures:
			ids.append(s.id)
			les.append(s.lecture_title)
			url.append(s.lecture_url)
			types.append(s.typee)

		print(les)
		data ={"lecture_id":ids,
			   "lecture_title":les,
			   "lecture_url": url,
			   "lecture_type":types
				}
		return JsonResponse(data)


@api_view(['GET'])
def reference_view(request, id ):

	if request.method == 'GET':
		reference = Reference.objects.filter(s_id= id)

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
def course_view(request, id ):

	if request.method == 'GET':
		course = Course.objects.filter(s_id= id)

		les=[]
		url=[]
		types=[]
		ids=[]

		for s in course:
			ids.append(s.id)
			les.append(s.course_name)
			url.append(s.course_url)
			types.append(s.typee[1])

		print(les)
		data = {"course_id":ids,
				"course_name":les,
				"course_url":url,
				"type":types
				}
		return JsonResponse(data)

@api_view(['GET'])
def addto_favourite_lecture_view(request, id ):

	if request.method == 'GET':
#hter is an exception dosenote exist
		L = Lecture.objects.get(id= id)
		L = Favourite_Lecture(lec_id =L)
		L.save()
		
		return JsonResponse({"response":"successfuly"})

@api_view(['GET'])
def get_favourite_lecture_view(request ):

	if request.method == 'GET':


		lecture = Favourite_Lecture.objects.all()

		les=[]
		url=[]

		for i in lecture:
			les.append(i.lec_id.lecture_title)
			url.append(i.lec_id.lecture_url)

		print(les)
		data ={"lecture_title":les,
			   "lecture_url": url
				}
		return JsonResponse(data)
##make it as a set in front for no repetition
###
@api_view(['GET'])
def addto_favourite_course_view(request, id ):

	if request.method == 'GET':

		C = Course.objects.get(id= id)
		C = Favourite_Course(cor_id = C)
		C.save()
		
		return JsonResponse({"response":"successfuly"})


@api_view(['GET'])
def get_favourite_course_view(request ):

	if request.method == 'GET':

		course = Favourite_Course.objects.all()

		les=[]
		url=[]

		for i in course:
			les.append(i.cor_id.course_name)
			url.append(i.cor_id.course_url)

		print(les)
		data ={"course_title":les,
			   "course_url": url
				}
		return JsonResponse(data)


