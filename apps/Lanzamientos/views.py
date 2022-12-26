from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Lanzamiento
from .forms import LanzamientoForm

# ---------- ---------- -------------           Vistas para el CRUD
class LanzamientoList (ListView):                    
    model = Lanzamiento
    template_name = 'Lanzamientos/lanzamientos_list.html'

class LanzamientoCreate (CreateView):
    model = Lanzamiento
    form_class = LanzamientoForm
    template_name = 'Lanzamientos/lanzamiento_form.html'
    success_url = reverse_lazy('lanzamientos_list')

class LanzamientoUpdate(UpdateView):
    model = Lanzamiento
    form_class = LanzamientoForm
    template_name = 'Lanzamientos/lanzamiento_form.html'
    success_url = reverse_lazy('lanzamientos_list')

class LanzamientoDelete(DeleteView):
    model = Lanzamiento
    template_name = 'Lanzamientos/lanzamiento_borrar.html'
    success_url = reverse_lazy('lanzamientos_list')

#----------------- ------------ >            Importaciones para la API 
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import LanzamientoSerializer


#---------------- ---------------- ---- Clases genericas para administración de API
class API_objects(generics.ListCreateAPIView):
    queryset = Lanzamiento.objects.all()
    serializer_class = LanzamientoSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lanzamiento.objects.all()
    serializer_class = LanzamientoSerializer

#---------------- ---------------- ---- Clases DEFINIDAS para administración de API

# El decorador @api_view verifica que la solicitud HTTP apropiada 
# se pase a la función de vista. En este momento, solo admitimos solicitudes GET
@api_view(['GET', 'POST'])
def lanzamiento_collection(request):
    if request.method == 'GET':
        lanzamientos = Lanzamiento.objects.all()
        serializer = LanzamientoSerializer(lanzamientos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LanzamientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def lanzamiento_element(request, pk):
    lanzamiento = get_object_or_404(Lanzamiento, id=pk)

    if request.method == 'GET':
        serializer = LanzamientoSerializer(lanzamiento)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        lanzamiento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        carrera_new = JSONParser().parse(request) 
        serializer = LanzamientoSerializer(lanzamiento, data=carrera_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
# Este código se activa cada vez que se 
# crea un nuevo usuario y se guarda en la base de datos.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


