from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    if not request.user.is_authenticated:
       return redirect('/admin') 
    return render(request, 'dashboard/index.html')