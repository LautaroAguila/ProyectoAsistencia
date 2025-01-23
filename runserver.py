import os
import django
from django.core.management import execute_from_command_line, call_command

# Configuración de entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asistencias.settings')

# Inicializar Django
django.setup()

# Ejecutar migraciones automáticamente
print("Ejecutando migraciones...")
call_command('migrate', interactive=False)
print("Migraciones completadas.")

# Iniciar el servidor sin autoreloader (para compatibilidad con PyInstaller)
print("Iniciando servidor...")
execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000', '--noreload'])
