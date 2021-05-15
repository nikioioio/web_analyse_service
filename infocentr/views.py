from django.views.generic import View,TemplateView
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json


class IndexPageView(View):
    template_name = 'infocentr/index.html'


    def get(self,request):
        return render(request,template_name=self.template_name)


class pl_mer(View):
    template_name = 'infocentr/pl_mer.html'


    def get(self,request):
        return render(request,template_name=self.template_name)


class ism(View):
    template_name = 'infocentr/ism.html'


    def get(self,request):
        return render(request,template_name=self.template_name)


class ism_doc(View):
    template_name = 'infocentr/ism_doc.html'


    def get(self,request):
        return render(request,template_name=self.template_name)

class card_process(View):
    template_name = 'infocentr/card_process.html'


    def get(self,request):
        return render(request,template_name=self.template_name)



