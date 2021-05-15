from django.views.generic import View,TemplateView
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json


class IndexPageView(View):
    template_name = 'news/index.html'


    def get(self,request):
        return render(request,template_name=self.template_name)





