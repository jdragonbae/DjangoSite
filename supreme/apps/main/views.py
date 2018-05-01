from django.shortcuts import render
from django.http import HttpResponse  
from django.views.generic import View

# Create your views here.
class MyView(View):
    template_name = 'main/index.html'

    def get(self, request):
        #return HttpResponse('result')
        return render(request, self.template_name)

    def post(self, requset):
        return HttpResponse('result')