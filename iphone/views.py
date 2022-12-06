from django.shortcuts import render

# Create your views here.
def iphone(request):
    return render (request, 'iphone.html')
