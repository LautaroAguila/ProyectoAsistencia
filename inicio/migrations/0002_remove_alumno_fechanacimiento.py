# Generated by Django 5.1.4 on 2025-02-25 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='fechaNacimiento',
        ),
    ]
