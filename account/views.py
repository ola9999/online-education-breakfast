from django.shortcuts import render
from account.serializers import (RegistrationSerializer,
								 SignInSerializer,
								 UsernameUpdateSerializer,
								 UsernameUpdateSerializer,
								 PasswordUpdateSerializer,
								 EmailUpdateSerializer,
								 )


from rest_framework import status	
from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from account.models import Account

# Create your views here.
#serializer.data.get('username')
@api_view(['POST'])
def registration_view(request):
	context = {}

	if request.method == 'POST':
		request_data =JSONParser().parse(request)
		serializer = RegistrationSerializer(data=request_data)

		if serializer.is_valid():
			account = serializer.save()

			context['response'] = 'successfully registered new user.'
			context['email'] = account.email
			context['username'] = account.username

		else:
			data = serializer.errors
			 
			return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)

		return JsonResponse(serializer.data , status=status.HTTP_201_CREATED)





@api_view(['POST'])
def sign_in_view(request):



	if request.method == 'POST':
		request_data =JSONParser().parse(request)
		print(request_data)
		serializer = SignInSerializer(data=request_data)
		print(serializer.is_valid())

		

	#	if serializer.is_valid():
			
	#		serializer_data=serializer.data
		try:
			serial_username = serializer.data.get("username")
			user_name = Account.objects.get(username= serial_username )#filter ( username )

		except Account.DoesNotExist:
			return  JsonResponse({'response': 'This user does not exist'}, status=status.HTTP_404_NOT_FOUND)

	
		serial_pass=serializer.data.get("password")
		pass_word = Account.objects.get(username=serializer.data.get('username')).password
		print(pass_word)
		print(serial_pass)
		if serial_pass == pass_word:
				return JsonResponse({'response' : 'login successfully'})

		elif serial_pass != pass_word :
				return JsonResponse({'response':'password is not correct'})
#
	
    #  if serializer.data.username == Account.objects.get(pk = pk)

#		account.password 
#		account.save()
#		return account


@api_view(['POST'])
def update_username_view(request,id):
	#old_name= bana

	if request.method == 'POST':
		request_data =JSONParser().parse(request)

		serializer = UsernameUpdateSerializer(data=request_data)

		if serializer.is_valid():

	     	# print(serializer.data.get('username'))

			new_username = serializer.data.get("username")

			user = Account.objects.get(id=id)

			# old_name = user.username
			user.username=  new_username

			user.save()

			return JsonResponse({"response":"username successfully updated"})




@api_view(['POST'])
def update_email_view(request,id):

	if request.method == 'POST':

		request_data =JSONParser().parse(request)

		serializer = EmailUpdateSerializer(data=request_data)

		print(serializer.is_valid())
	    # serializer.is_valid():

		new_email = serializer.data.get("email")

		user = Account.objects.get(id=id)
		# old_name = user.username
		user.email=  new_email

		print(Account.objects.get(id=id).email)

		user.save()

		return JsonResponse({"response":"email successfully updated"})

		if serializer.is_valid() == false :
			data = serializer.errors
			return JsonResponse(data)


	

@api_view(['POST'])
def update_password_view(request,id):

	if request.method == 'POST':
		request_data =JSONParser().parse(request)

		serializer = PasswordUpdateSerializer(data=request_data)

		if serializer.is_valid():

	     	# print(serializer.data.get('username'))

			new_pass = serializer.data.get("password")

			pass_word = Account.objects.get(id=id)

			# old_name = user.username
			pass_word.password=  new_pass

			pass_word.save()

			return JsonResponse({"response":"password successfully updated"})

		

		

@api_view(['POST'])
def update_profile_view(request,id):
	if request.method == 'POST':
		request_data =JSONParser().parse(request)
		print(request_data)
		serializer = ProfileUpdateSerializer(data=request_data)

		

