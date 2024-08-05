"""SecuritySystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from securityapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('signup/',signup,name="signup"),
    path('login/',Login,name="login"),
    path('security_form/',security_form,name="security_form"),
    path('admin_index/',admin_index,name="admin_index"),
    path('admin_login/',admin_login,name="admin_login"),
    path('logout_admin/',logout_admin,name="logout_admin"),
    path('total_applications/',total_applications,name="total_applications"),
    path('bookingdetails/<int:pid>/',bookingdetails,name="bookingdetails"),
    path('accepted_applications/',accepted_applications,name="accepted_applications"),
    path('rejected_applications/',rejected_applications,name="rejected_applications"),
    path('delete_guard/<int:pid>/',delete_guard,name="delete_guard"),
    path('total_guards/',total_guards,name="total_guards"),
    path('work_details/<int:pid>/',work_details,name="work_details"),
    path('profile_update/',profile_update,name="profile_update"),
    path('change_password/',change_password,name="change_password"),
    path('guard_profile/',guard_profile,name="guard_profile"),
    path('profile_update2/<int:pid>/',profile_update2,name="profile_update2"),
    path('change_password2/<int:pid>/',change_password2,name="change_password2"),
    path('training_level/<int:pid>/',training_level,name="training_level"),
    path('training_details/<int:pid>/',training_details,name="training_details"),
    path('issues/<int:pid>/',issues,name="issues"),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)