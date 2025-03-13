import os
import django
from django.core.management import execute_from_command_line, call_command

# Configuración de entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asistencias.settings')
django.setup()

# Ejecutar migraciones automáticamente
print("Verificando y aplicando migraciones...")
call_command('makemigrations', 'inicio', interactive=False)  # Asegurar que las migraciones están generadas
call_command('migrate', interactive=False)  # Aplicar las migraciones pendientes
print("Migraciones completadas.")

# Iniciar el servidor
print("Iniciando servidor...")
execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000', '--noreload'])

#ERROR migraciones, borro la bd y las hago de nuevo
    ## 🔥 Eliminar base de datos
    #db_path = Path("db.sqlite3")
    #if db_path.exists():
    #    print("⚠ Eliminando base de datos antigua...")
    #    db_path.unlink()
    #
    ## 🔥 Eliminar migraciones previas
    #migrations_dir = Path("inicio/migrations")
    #if migrations_dir.exists():
    #    for file in migrations_dir.glob("000*.py"):  # Borra todas las migraciones excepto __init__.py
    #        file.unlink()
    #    print("✅ Migraciones previas eliminadas.")
