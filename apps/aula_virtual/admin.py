from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class PersonaResource(resources.ModelResource):
    class Meta:
        model= Persona

class DocenteResource(resources.ModelResource):
    class Meta:
        model= Docente

class AlumnoResource(resources.ModelResource):
    class Meta:
        model= Alumno

class CursoResource(resources.ModelResource):
    class Meta:
        model= Curso

class Detalle_alumno_en_cursoResource(resources.ModelResource):
    class Meta:
        model= Detalle_alumno_en_curso

class AsistenciaResource(resources.ModelResource):
    class Meta:
        model= Asistencia



class PersonaAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields = ['dni','nombre','apellido_paterno', 'apellido_materno']
    
    resource_class= PersonaResource
    
class DocenteAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    resource_class= DocenteResource
    
class AlumnoAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    resource_class= AlumnoResource
    
class CursoAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields= ['etiqueta','nombre_curso',]
    resource_class= CursoResource
    
class Detalle_alumno_en_cursoAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    resource_class= Detalle_alumno_en_cursoResource
    
class AsistenciaAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    resource_class= AsistenciaResource
    
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('nombre_institucion','direccion',)

 
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Periodo)
admin.site.register(Nivel)
admin.site.register(Grado)
admin.site.register(Seccion)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Docente, PersonaAdmin)
admin.site.register(Alumno, PersonaAdmin)
admin.site.register(Curso, PersonaAdmin)
admin.site.register(Detalle_alumno_en_curso, PersonaAdmin)
admin.site.register(Asistencia, PersonaAdmin)
admin.site.register(Contenido)
admin.site.register(Carpeta)
admin.site.register(Archivo)
