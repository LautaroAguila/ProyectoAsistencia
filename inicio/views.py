from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import *
from inicio.models import Alumno, Escuela
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404


class CrearAlumno(CreateView):
    model = Alumno
    template_name = "inicio/alumno/crear_alumno.html"
    success_url = reverse_lazy('inicio:listado_alumnos')
    fields = ['nombre', 'apellido', 'escuela', 'dias', 'turno_profesor']

class ListadoAlumnos(ListView):
    model = Alumno
    template_name = "inicio/alumno/listado_alumnos.html"
    context_object_name = 'alumnos'

    def get_queryset(self):
        # Obtener el turno guardado en la sesión
        turno_profesor = self.request.session.get('turno_profesor')

        # Si no hay turno seleccionado, no mostrar alumnos
        if not turno_profesor:
            return Alumno.objects.none()

        # Filtrar los alumnos según el turno del profesor
        queryset = Alumno.objects.filter(turno_profesor=turno_profesor)

        # Obtener el parámetro de ordenamiento
        orden = self.request.GET.get('orden', 'id')  # Por defecto se ordena por ID

        # Validar las opciones de ordenamiento permitidas
        opciones_validas = ['escuela', '-escuela', 'apellido', '-apellido']
        if orden not in opciones_validas:
            orden = 'id'

        # Retornar el conjunto de datos filtrado y ordenado
        return queryset.order_by(orden)

class VerAlumno(DetailView):
    model = Alumno
    template_name = "inicio/alumno/ver_alumno.html"

class EditarAlumno(UpdateView):
    model = Alumno
    template_name = "inicio/alumno/editar_alumno.html"
    success_url = reverse_lazy('inicio:listado_alumnos')
    fields = ['nombre','apellido','grado','edad','turno','dni','grupo_familiar','tel_contacto','nombre_tutor','dni_tutor','escuela','dias','asistencias','inasistencias','profesionales','observaciones']

class EliminarAlumno(DeleteView):
    model = Alumno
    template_name = "inicio/alumno/eliminar_alumno.html"
    success_url = reverse_lazy('inicio:listado_alumnos')

def ver_escuela(request, escuela_numero): 
    try:
        # Filtrar la escuela basada en el campo 'numero'
        escuela = get_object_or_404(Escuela, numero=escuela_numero)
        # Renderizar la plantilla si se encuentra la escuela
        return render(request, 'inicio/escuela/ver_escuela.html', {'escuela': escuela})
    except:
        # Renderizar una plantilla de error si no se encuentra
        return render(request, 'inicio/escuela/escuela_no_creada.html', {'escuela_id': escuela_numero})

class CrearEscuela(CreateView):
    model = Escuela
    template_name = "inicio/escuela/crear_escuela.html"
    success_url = reverse_lazy('inicio:listado_alumnos')
    fields = ['nombre_escuela','numero','direccion','tel_escuela' ,'mail_escuela' ,'nombre_directivo']

def vaciar_escuelas(request):
    if request.method == 'POST':
        Escuela.objects.all().delete()  # Vaciar todas las escuelas
        return redirect('inicio:listado_alumnos')  # Redirige a la lista de alumnos o a otra página

    return render(request, 'inicio/escuela/vaciar_escuelas.html')

def seleccionar_turno(request):
    if request.method == 'POST':
        # Obtener el turno enviado desde el formulario
        turno = request.POST.get('turno')

        # Validar si el turno es válido (T o M)
        if turno in ['T', 'M']:
            request.session['turno_profesor'] = turno  # Guardar el turno en la sesión
            return redirect('inicio:listado_alumnos')  # Redirigir al listado de alumnos

    # Renderizar el formulario de selección
    return render(request, 'inicio/seleccionar_turno.html')

