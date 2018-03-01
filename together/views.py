from django.http import HttpResponse
from django.shortcuts import render

#define home page
def homepage(request):
	return render(request,'homepage.html')

#define trang about
def about(request):
	#return HttpResponse('about')
	return render(request,'about.html')