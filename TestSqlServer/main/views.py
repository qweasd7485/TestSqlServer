from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
   context = {'like':'Django is good!'}
   return render(request, 'main/main.html', context)
    
def about(request):
    return render(request, 'main/about.html')
    