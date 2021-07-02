from django.db import models

class Subject(models.Model):

    subject_name =  models.CharField(max_length=200)
    year		 = models.CharField(max_length=10)
    semister	 = models.CharField(max_length=10)

	

#subject1 : multimedia
#subject2 :OS1
#subject3: parallel	
# Subject4 :
# Subject5:
# Subject6
# Subject7
# Subject8
# Subject9
# Subject10
# Subject11
# Subject12

class Lecture(models.Model):
    s_id 			= models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='lec')

    lecture_title	= models.CharField(max_length=200)
    lecture_url 	= models.CharField(max_length=200)

class Reference(models.Model):
    s_id = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True,default=None,related_name='ref')
    # lec_id			= models.OneToManyField(Lecture,blank=True)
    reference_name	= models.CharField(max_length=200)
    reference_url	= models.CharField(max_length=200)

class Courses(models.Model):
    s_id 		= models.ForeignKey(Subject, on_delete=models.CASCADE,null=True,default=None,related_name='Cor')
    course_name  = models.CharField(max_length=200)
    # lec_id =  models.ForeignKey(Lecture, on_delete=models.CASCADE,null=True,default=None)

    course_url 		= models.CharField(max_length=200)
