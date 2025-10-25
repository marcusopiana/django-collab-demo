from django.shortcuts import render

# Create your views here.
def home(request):
    
    context = {}
    return render(request,'myapp/home.html',context)

def about(request):
    context = {}
    return render(request,'myapp/about.html',context)