from django.contrib import admin
from account.models import Account,Profile
# Register your models here.

class Accountadmin(admin.ModelAdmin):
	list_display = ('email' , 'username' ,'password',)

class Profileadmin(admin.ModelAdmin):
	list_display = ('user' ,'image',)



# admin.site.register(C)

admin.site.register(Account,Accountadmin)
admin.site.register(Profile,Profileadmin)