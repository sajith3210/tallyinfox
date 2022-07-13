from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'index.html')

def stockgroup(request):
    return render(request,'stock group creation.html')
