from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def L2Daily(request):
   context = {'like':'Django is good!'}
   return render(request, 'L2Daily/L2Daily.html', context)
