from django.shortcuts import render

# Create your views here.

def index (request):
    context = {}
    return render (request,'caosnews/index.html',context)

def categorias (request):
    context = {}
    return render (request,'caosnews/categorias.html',context)

def periodistas (request):
    context = {}
    return render (request,'caosnews/periodistas.html',context)

def contacto (request):
    context = {}
    return render (request,'caosnews/contacto.html',context)