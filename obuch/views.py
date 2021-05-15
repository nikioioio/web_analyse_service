from django.views.generic import View,TemplateView
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json


class IndexPageView(View):
    template_name = 'obuch/index.html'


    def get(self,request):
        return render(request,template_name=self.template_name)



class calendar(View):
    template_name = 'obuch/calendar.html'


    def get(self,request):
        return render(request,template_name=self.template_name)



class present(View):
    template_name = 'obuch/present.html'


    def get(self,request):
        return render(request,template_name=self.template_name)






