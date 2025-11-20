"""
URL configuration for educationalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from educationalapplication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view, name='home'),
    path('adminpage/', views.adminpage_view, name='adminpage'),
    path('classix/', views.classix_view, name='classix'),
    path('classviii/', views.classviii_view, name='classviii'),
    path('classx/', views.classx_view, name='classx'),
    path('contactus/', views.contactus_view, name='contactus'),
    path('latestnews/', views.latestnews_view, name='latestnews'),
    path('parentreg/', views.parentreg_view, name='parentreg'),
    path('photos/', views.photos_view, name='photos'),
    path('vedios/', views.vedios_view, name='vedios'),
    path('about/', views.about_view, name='about'),
]
