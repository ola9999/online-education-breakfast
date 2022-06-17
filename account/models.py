from django.db import models

# Create your models here.


class Account(models.Model):

	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	password				= models.CharField(max_length=30,default = None)
	

 #   image 					= models.ImageField(default='default.jpg', upload_to='profile_pics')

#	profile_image 			= models.ImageField(max_Length= 255 , upload_to= get_profile_image_filepath , null = True ,blank= True, default =get_default_profile_image )

	# def __str__(self):
	# 	return ['id','email', 'username', 'password' ,]
	# def __str__(self):
	#         return self.subject_name
	

class Profile(models.Model):
#	account = models.ForeignKey(Account, on_delete=models.CASCADE)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


      # Profile.objects.get(user=get(Account.objects.get(username='sana'))
      # Profile.objects.get(user=x)