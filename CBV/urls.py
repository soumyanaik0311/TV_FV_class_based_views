"""
URL configuration for CBV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('String_FBV/',String_FBV,name='String_FBV'),
    path('String_CBV/',String_CBV.as_view(),name='String_CBV'),

    path("FBV_file/",FBV_file,name='FBV_file'),
    path("CBV_file/",CBV_file.as_view(),name='CBV_file'),

    path("SFValidationbyFBV/",SFValidationbyFBV,name='SFValidationbyFBV'),
    path("SFValidationbyCBV/",SFValidationbyCBV.as_view(),name='SFValidationbyCBV'),


    path("HtmlByTV/",TemplateView.as_view(template_name='HtmlByTV.html'),name='HtmlByTV'),
    path("SendDataByTV/",SendDataByTV.as_view(),name='SendDataByTV'),

    path("ISByFV/",ISByFV.as_view(),name='ISByFV'),
    path("ISByFVstr/",ISByFVstr.as_view(),name='ISByFVstr'),
    


   

]
