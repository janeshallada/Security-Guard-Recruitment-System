"""OnlineSecurityGuardsHiringSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from securityapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('admin_login/', admin_login, name="admin_login"),
    path('admin_profile/', admin_profile, name="admin_profile"),
    path('logout_admin/', logout_admin, name="logout_admin"),
    path('dashboard/', dashboard, name="dashboard"),
    path('add_security_guard/', add_security_guard, name="add_security_guard"),
    path('manage_security_guard/', manage_security_guard, name="manage_security_guard"),
    path('edit_security_guard/<int:pid>/', edit_security_guard, name="edit_security_guard"),
    path('change_password/', change_password, name="change_password"),
    path('hiring_form/', hiring_form, name="hiring_form"),
    path('request_status/', request_status, name="request_status"),
    path('booking_detail/<int:pid>/', booking_detail, name="booking_detail"),
    path('detail_booking/<int:pid>/', detail_booking, name="detail_booking"),
    path('bookinglist/', bookinglist, name="bookinglist"),
    path('delete_booking/<int:pid>/', delete_booking, name="delete_booking"),
    path('delete_security_guard/<int:pid>/', delete_security_guard, name="delete_security_guard"),
    path('report/', report, name="report"),
    path('search_report/', search_report, name="search_report"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
