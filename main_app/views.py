
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import json
from django.shortcuts import render,HttpResponse

class IndexPageView(View):
    template_name = 'main_app/index.html'
    def get(self,request):
        return render(request,template_name=self.template_name)








# Create your views here.

