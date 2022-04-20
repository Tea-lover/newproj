from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'hello/index.html')
def about (request):
    return HttpResponse("<h2>About</h2>")
# Create your views here.
