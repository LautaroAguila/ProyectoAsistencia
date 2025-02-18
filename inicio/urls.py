from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.seleccionar_turno, name='seleccionar_turno'),
    path('alumnos/crear/', views.CrearAlumno.as_view(), name='crear_alumno'),
    path('alumnos/', views.ListadoAlumnos.as_view(), name='listado_alumnos'),
    path('alumnos/<int:pk>/', views.VerAlumno.as_view(), name='ver_alumno'),
    path('alumnos/<int:pk>/editar/', views.EditarAlumno.as_view(), name='editar_alumno'),
    path('alumnos/<int:pk>/eliminar/', views.EliminarAlumno.as_view(), name='eliminar_alumno'),
    path('escuela/<int:escuela_numero>/', views.ver_escuela, name='ver_escuela'),
    path('escuela/crear/', views.CrearEscuela.as_view(), name='crear_escuela'),
    path('escuela/vaciar_escuelas/', views.vaciar_escuelas, name='vaciar_escuelas'),
    path('export/excel/', views.export_alumnos_excel, name='export_excel')
]


