from django.http import HttpResponse, request
from django.shortcuts import render
from .models import Place, Members


# Create your views here.
def demo(request):
     obj=Place.objects.all()
     obj2=Members.objects.all()
     return render(request,'index.html',{'result':obj,'res':obj2})

#def about(request):
   # return render(request,"about.html")
#def content(request):
  #  return HttpResponse("hello everyone am content")
#def addition(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # res=x+y
    #return render(request,"result.html",{'result':res})