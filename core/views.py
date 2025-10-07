from django.shortcuts import render

# Create your views here.
def home_macrosul(request):
    return render(request,'home_macrosul.html')

def home_medicina(request):
    return render(request,'home_linhas.html')

def home_veterinaria(request):
    return render(request,'home_linhas.html')

def home_esportes(request):
    return render(request,'home_linhas.html')

def home_cosmeticos(request):
    return render(request,'home_linhas.html')