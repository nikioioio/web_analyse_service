from django.views.generic import View,TemplateView
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json


class IndexPageView(View):
    template_name = 'reports/index.html'


    def get(self,request):
        return render(request,template_name=self.template_name)



class reports_one(View):
    template_name = 'reports/reports_one.html'


    def get(self,request):
        return render(request,template_name=self.template_name)


class reports_two(View):
    template_name = 'reports/reports_two.html'


    def get(self,request):
        return render(request,template_name=self.template_name)


class reports_three(View):
    template_name = 'reports/reports_three.html'


    def get(self,request):
        return render(request,template_name=self.template_name)



class rep_template(View):
    template_name = 'reports/rep_template.html'


    def get(self,request):
        return render(request,template_name=self.template_name)



class reports_four(View):
    template_name = 'reports/reports_four.html'


    def get(self,request):
        return render(request,template_name=self.template_name)

