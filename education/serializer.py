from rest_framework import serializers

from education.models import Subject,Lecture,Reference,Courses

class SubjectSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ['subject_name', 'year','semister' ,]#, 'password2']#' __all__ '#
