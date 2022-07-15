from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'index.html')

def stockgroup(request):
    return render(request,'stock group creation.html')

def stockcategory(request):
    return render(request,'stock category creation.html')

def stockitem(request):
    return render(request,'stock item creation.html')

def unitalter(request):
    return render(request,'unit alteration.html')

def locationalter(request):
    return render(request,'Location alteration.html')

def companypricelevel(request):
    return render(request,'company price level.html')
