from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hi(req):
    return render(req , 'index.html' , { 'namer' : 'getter'})