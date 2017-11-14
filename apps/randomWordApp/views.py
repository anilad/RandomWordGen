from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    if not 'key' in request.session:
        request.session['key']=1
    randomStr = get_random_string(length=14)
    context={
        "number": request.session['key'],
        "randomStr": randomStr,
    }
    return render(request,'randomWordApp/index.html', context)

def process(request):
    request.session['key']+= 1
    return redirect('/')