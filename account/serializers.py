from rest_framework import serializers

from account.models import Account,Profile


class RegistrationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ['id','email', 'username', 'password' ,]#, 'password2']#' __all__ '#

#	password2 				= serializers.CharField( max_length=60)
#	password 				= serializers.CharField( max_length=60)

	
class SignInSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ['id','username', 'password' ,]#, 'password2']#' __all__ '#

class UsernameUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username',]


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['image',]

class PasswordUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['password',]

class EmailUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['email',]


		

#	def	is_pass_valid(password ,password2 ):

#		if password != password2:
#			return False
			
#		return True
 



