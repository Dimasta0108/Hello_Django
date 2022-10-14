from django.http import HttpResponse
from django.shortcuts import render

a = 5+6
def about(request):
    return render(request,'about.html', {'gretting':a})

def home(request):
    return HttpResponse('This is my home')

