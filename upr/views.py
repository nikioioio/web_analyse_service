from django.views.generic import View,TemplateView
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json


class IndexPageView(View):
    template_name = 'upr/index.html'


    def get(self,request):
        return render(request,template_name=self.template_name)


class ruk(View):
    template_name = 'upr/ruk.html'


    def get(self,request):
        return render(request,template_name=self.template_name)


class struct(View):
    template_name = 'upr/str_upr.html'


    def get(self,request):
        return render(request,template_name=self.template_name)


class polozh(View):
    template_name = 'upr/polozh_ob_upr.html'


    def get(self,request):
        return render(request,template_name=self.template_name)