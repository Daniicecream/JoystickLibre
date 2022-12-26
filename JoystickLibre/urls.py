"""JoystickLibre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token  

urlpatterns = [
    
    #rutas para apps
    path('admin/', admin.site.urls),
    path('lanzamientos/', include('apps.Lanzamientos.urls')),
    path('usuario/', include('apps.Usuario.urls')),
    
    #rutas generales
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('nosotros', TemplateView.as_view(template_name='nosotros.html'), name='nosotros'),
    path('reseñas', TemplateView.as_view(template_name='reseñas.html'), name='reseñas'),
    path('opiniones', TemplateView.as_view(template_name='opiniones.html'), name='opiniones'),
    path('armas', TemplateView.as_view(template_name='armas.html'), name='armas'),
    path('contacto', TemplateView.as_view(template_name='contacto.html'), name='contacto'),
    path('entrada', TemplateView.as_view(template_name='entrada.html'), name='entrada'),

    # Login and Logout 
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),

    # Para pedir token con usuario y password
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
]
