from django.shortcuts import render

# Create your views here.
def home_macrosul(request):
    return render(request,'home.html')

def home_medicina(request):
    return render(request,'home.html')

def home_veterinaria(request):
    return render(request,'home.html')

def home_esportes(request):
    return render(request,'home.html')

def home_cosmeticos(request):
    return render(request,'home.html')