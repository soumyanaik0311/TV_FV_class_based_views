from typing import Any
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View, TemplateView, FormView
from app.forms import *


#returning string as response By CBV
def String_FBV(request):
    return HttpResponse('String response by FBV')


#returning string as response By CBV
class String_CBV(View):
    def get(self,request):
        return HttpResponse('String response by CBV')


#returning HTML File as response By FBV
def FBV_file(request):
    return render(request,'FBV_file.html')


#returning HTML File as response By CBV
class CBV_file(View):
    def get(self,request):
        return render(request,'CBV_file.html')


def SFValidationbyFBV(request):
    ESFO=StudentMF()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Student details created !')
        else:
            return HttpResponse('Invalid details !')
    return render(request,'SFValidationbyFBV.html',d)

class SFValidationbyCBV(View):
    def get(self,request):
        ESFO=StudentMF()
        d={'ESFO':ESFO}
        return render(request,'SFValidationbyCBV.html',d)
    def post(self,request):
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Student details created !')
        else:
            return HttpResponse('Invalid details !')


# without using view class we can send the html file by url mapping

# class HtmlByTV(TemplateView):
#     template_name='HtmlByTV.html'

# sending data along with html page so templateview is inefficient, we need to use get_context_data for creating empty context dictionary object
class SendDataByTV(TemplateView):
    template_name='SendDataByTV.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ESDO=super().get_context_data(**kwargs)
        ESDO['Name']='Name: Soumya Ranjan Naik'
        ESDO['Age']='Age: 23'
        ESDO['ESFO']=StudentMF()
        return ESDO
    
    def post(self,request):
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Student details created')
        else:
            return HttpResponse('Invalid Details')


class ISByFV(FormView):
    template_name='ISByFV.html'
    form_class=StudentMF

    def form_valid(self, form):
        form.save()
        return HttpResponse('Student details Submitted')
    
class ISByFVstr(FormView):
    template_name='ISByFV.html'
    form_class=StudentMF

    def form_valid(self, form):
        data=form.cleaned_data
        return HttpResponse(str(data))
    
