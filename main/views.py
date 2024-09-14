from django.shortcuts import render

def Home(request):

    return render(request, "home.html")

def Shop(request):

    return render(request, "shop.html")

def Equipo(request):

    return render(request, "about.html")

def Documentacion(request):

    return render(request, "documentacion.html")

def MapaEstrategico(request):

    return render(request, "mapa_estrategico.html")

def Indicadores(request):

    return render(request, "indicadores.html")

def CuatroPs(request):

    return render(request, "mapa_estrategico.html")