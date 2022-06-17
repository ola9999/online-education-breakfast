from django.db import models
from account.models import Account

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
# # Subject12
    def __str__(self):
            return 'Subject: ' + self.subject_name

from django.utils.translation import gettext_lazy as _



class Lecture(models.Model):

    class Types(models.TextChoices):
        ACADEMIC =   'academic' ,    _('academic')
        FUNCTIONAL = 'functional' ,    _('functional')

    s_id 			= models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='lec')

    lecture_title	= models.CharField(max_length=200)
    lecture_url 	= models.CharField(max_length=200)
    typee           = models.CharField(max_length=200,
                                        # choices=[x.value for x in STATUS],
                                        choices = Types.choices,
                                         # default= STATUS.get_value(STATUS.academic)
                                        default =  Types.ACADEMIC,
                                        null=False)

    def __str__(self):
            return 'Lecture: ' + self.lecture_title

class Reference(models.Model):

    s_id = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True,default=None,related_name='ref')
    # lec_id			= models.OneToManyField(Lecture,blank=True)
    reference_name	= models.CharField(max_length=200)
    reference_url	= models.CharField(max_length=200)

    def __str__(self):
            return 'Reference: ' + self.reference_name

class Course(models.Model):
    # MY_CHOICES = (
    #             ('a','global'),
    #             ('b','python'),
    #             ('c','java'),
    #             ('d','css'),
    #             ('e','c++'),
    #             ('f','c#'),
    #             ('g','html'),
    #              )

    class Types(models.TextChoices):
            GLOBAL =   'global', _('global')
            PYTHON =   'python', _('python')
            java =     'java', _('java')
            css  =     'css', _('css')
            c_plus =   'c++', _('c++')
            c_sharp =  'c#', _('c#')
            html =     'html', _('html')


    s_id 		 = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True,default=None,related_name='Cor')
    course_name  = models.CharField(max_length=200)
    # lec_id =  models.ForeignKey(Lecture, on_delete=models.CASCADE,null=True,default=None)

    course_url   = models.CharField(max_length=200)
    typee        = models.CharField(max_length=200,choices=Types.choices, default= Types.GLOBAL,null=False)

    def __str__(self):
            return 'Course: ' + self.course_name



class Favourite_Lecture(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,default=None)

    lec_id = models.ForeignKey(Lecture, on_delete=models.CASCADE,null=True,default=None)

    def __str__(self):
            return 'Lecture: ' + self.lec_id.lecture_title


class Favourite_Course(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,default=None)

    cor_id = models.ForeignKey(Course, on_delete=models.CASCADE,null=True,default=None)

    def __str__(self):
            return 'Course: ' + self.cor_id.course_name
# class Summary(models.Model):
#     s_id        = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True,default=None,related_name='Cor')
#     summary_name  = models.CharField(max_length=200)
#     summary_url      = models.CharField(max_length=200)

# class C(models.Model):

#     MY_CHOICES = (
#         ('a', 'Hola'),
#         ('b', 'Hello'),
#         ('c', 'Bonjour'),
#         ('d', 'Boas'),
#     )

#     my_field = models.CharField(max_length=1, choices=MY_CHOICES, default= 'global',null=False)
    




    # MY_CHOICES = (
    #             (1,'academic'),
    #             (2,'functional'),
    #             )


    # class STATUS(Enum):
    #     academic = (1, 'academic')
    #     functional = (2, 'functional')

    #     @classmethod
    #     def get_value(cls , member):
    #         return member.value[0]
