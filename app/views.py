from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def sample(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        SO=Sample.objects.get_or_create(username=name, email=email)
        if SO:
            return HttpResponse("Details newely added")
        else:
            return HttpResponse("Something went wrong")

    return render(request,'sample.html')