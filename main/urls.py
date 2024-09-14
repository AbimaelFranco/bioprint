from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home, name="Home"),
    path('shop', views.Shop, name="Shop"),
    path('equipo', views.Equipo, name="Equipo"),
    path('documentacion', views.Documentacion, name="Documentacion"),
    path('mapa', views.MapaEstrategico, name="Mapa"),
    path('indicadores', views.Indicadores, name="Indicadores"),
    path('cuatrops', views.CuatroPs, name="CuatroPs"),
    # path('dashboard_info', views.DashboardInfo, name="Dashboard_info"),
    # path('login', views.Login, name="Login"),
    # path('faqs', views.FAQs, name="FAQs"),
    # path('contacto', views.Contacto, name="Contacto"),
    # path('cerrar_sesion', views.cerrar_sesion, name="Cerrar_sesion"),
]