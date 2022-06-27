from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class PersonaResource(resources.ModelResource):
    class Meta:
        model= Persona


class CursoResource(resources.ModelResource):
    class Meta:
        model= Curso

class Detalle_alumno_en_cursoResource(resources.ModelResource):
    class Meta:
        model= Detalle_alumno_en_curso

class AsistenciaResource(resources.ModelResource):
    class Meta:
        model= Asistencia
        
class ArchivoResource(resources.ModelResource):
    class Meta:
        model= Archivo


class PersonaAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields = ['dni','nombre','apellido_paterno', 'apellido_materno']
    list_display = ('id','nombre','apellido_paterno', 'apellido_materno', 'dni', 'fecha_nacimiento', 'genero',)

    resource_class= PersonaResource
    
    
class CursoAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields= ['etiqueta','nombre_curso',]
    list_display = ('id','etiqueta','nombre_curso','nivel','grado','seccion','periodo')
    resource_class= CursoResource
    
class Detalle_alumno_en_cursoAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display=('id','usuario', 'curso')
    resource_class= Detalle_alumno_en_cursoResource
    
class AsistenciaAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ('id','detalle_alumno_en_curso', 'fecha')
    resource_class= AsistenciaResource
    
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_institucion','direccion','telefono',)

class ArchivoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields= ['nombre_archivo','carpeta',]
    list_display = ('id','carpeta','nombre_archivo','visibilidad_alumno',)
    resource_class = ArchivoResource
 
class CarpetaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_folder','curso','contenido','es_tarea')
    
class ContenidoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo',)
 
class GradoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_grado',)
 
class SeccionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_seccion',)
    
class NivelAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_nivel',)
    
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('id','fecha_inicio', 'fecha_fin',)
    
    
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Nivel, NivelAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Detalle_alumno_en_curso, Detalle_alumno_en_cursoAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(Contenido, ContenidoAdmin)
admin.site.register(Carpeta,CarpetaAdmin)
admin.site.register(Archivo,ArchivoAdmin)
