"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account.views import (registration_view, 
                           sign_in_view,
                           update_username_view,
                           update_email_view,
                           update_password_view,
                           update_profile_view)


from education .views import (subject_view,
                              lecture_view,
                              reference_view,
                              course_view,
                              addto_favourite_lecture_view,
                              get_favourite_lecture_view,
                              addto_favourite_course_view,
                              get_favourite_course_view)


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', registration_view, name='registration_view'),
    path('signin/', sign_in_view, name='sign_in_view'),

    path('update_username/<int:id>', update_username_view, name='update_username_view'),
    path('update_email/<int:id>', update_email_view, name='update_email_view'),
    path('update_password/<int:id>', update_password_view, name='update_password_view'),
    path('update_profile_pic/<int:id>', update_profile_view, name='update_profile_view'),




#id=year
    path('subjects/<int:id>/', subject_view, name='subject_view'),

# id=subject_id
    path('lectures/<int:id>/', lecture_view, name='lecture_view'),
    path('references/<int:id>/', reference_view, name='reference_view'),
    path('course/<int:id>/', course_view, name='course_view'),

    path('course/<int:id>/', course_view, name='course_view'),
##
    path('addtofavourite_lecture/<int:id>/', addto_favourite_lecture_view, name='addto_favourite_lecture_view'),
    path('get_favourite_lecture/', get_favourite_lecture_view, name='get_favourite_lecture_view'),
##
    path('addto_favourite_course/<int:id>/', addto_favourite_course_view, name='addto_favourite_course_view'),
    path('get_favourite_course/', get_favourite_course_view, name='get_favourite_course_view'),


    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
