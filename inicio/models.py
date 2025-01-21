from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(default='', max_length=20)
    apellido = models.CharField(default='', max_length=20)
    edad = models.IntegerField(default=0)
    escuela = models.IntegerField(default=0)
    grado = models.IntegerField(default=0)
    turno = models.CharField(default='', max_length=1)
    dni = models.IntegerField(default=0)
    grupo_familiar = models.CharField(default='', max_length=50)
    tel_contacto = models.IntegerField(default=0)
    nombre_tutor = models.CharField(default='', max_length=20)
    dni_tutor = models.IntegerField(default=0)
    dias = models.IntegerField(default=0)
    asistencias = models.IntegerField(default=0)
    inasistencias = models.IntegerField(default=0)
    profesionales = models.CharField(default='', max_length=1000)
    observaciones = models.TextField(default='')

    turno_profesor = models.CharField(default='T', choices=[('M', 'Mañana') , ('T', 'Tarde')], max_length=1)


    @property
    def porcentaje(self):
        total_dias = self.asistencias + self.inasistencias
        if total_dias == 0:  # Evitar división por cero
            return 0
        return (self.asistencias * 100) / total_dias
    
    def __str__(self):
        return f'{self.nombre} tiene una asistencia del {self.porcentaje:.1f}%'


class Escuela(models.Model):
    nombre_escuela = models.CharField(default='', max_length=30)
    numero = models.IntegerField(default=0)
    direccion = models.CharField(default='', max_length=30)
    tel_escuela = models.IntegerField(default=0)
    mail_escuela = models.CharField(default='', max_length=30)
    nombre_directivo = models.CharField(default='', max_length=30)
    def __str__(self):
        return f' {self.nombre_escuela} es la numero {self.numero}%'

