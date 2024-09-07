from django.shortcuts import render

def Home(request):

    return render(request, "home.html")

def Shop(request):

    return render(request, "shop.html")

def Equipo(request):

    return render(request, "about.html")