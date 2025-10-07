from django.contrib import admin
from django.urls import path
from core.views import home_cosmeticos, home_esportes, home_macrosul, home_medicina, home_veterinaria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_macrosul, name="home_macrosul"),
    path('home_veterinaria',home_veterinaria, name="home_veterinaria"),
    path('home_medicina',home_medicina, name="home_medicina"),
    path('home_esportes',home_esportes, name="home_esportes"),
    path('home_cosmeticos',home_cosmeticos, name="home_cosmeticos"),
]
