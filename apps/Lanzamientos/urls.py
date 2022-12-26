from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import LanzamientoList, LanzamientoCreate, LanzamientoUpdate, LanzamientoDelete
from django.contrib.auth.views import login_required

#Para retornar el Json (API)
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Lanzamientos import views


urlpatterns = [
    path('listar/', LanzamientoList.as_view(), name="lanzamientos_list"),
    path('crear/', login_required(LanzamientoCreate.as_view()), name="lanzamiento_form"),
    path('editar/<int:pk>', login_required(LanzamientoUpdate.as_view()), name="lanzamientos_update"),
    path('borrar/<int:pk>', login_required(LanzamientoDelete.as_view()), name="lanzamientos_delete"),
]

urlpatterns += [
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
    
    #API
    path('coleccion/',  views.lanzamiento_collection , name='lanzamiento_collection'),
    path('elemento/<int:pk>/', views.lanzamiento_element ,name='lanzamiento_element'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
