from django.shortcuts import render

# Create your views here.
def home(request):
    
    context = {}
    return render(request,'myapp/home.html',context)

def about(request):
    context = {}
    return render(request,'myapp/about.html',context)

def contact(request):
    context = {}
    return render(request,'myapp/contact.html',context)

# def memorandums(request):
#     context = {}
#     return render(request,'myapp/memorandums.html',context)

# sudo apt update
# sudo apt install git-lfs -y
# git lfs install