from pyexpat import model
from django.db import models

from django.contrib.auth.models import User

class Institucion(models.Model):
    direccion = models.CharField(verbose_name="Dirección", max_length=100)
    email = models.EmailField(verbose_name="Correo Electrónico", max_length=50)
    nombre_institucion = models.CharField(verbose_name="Nombre de la Institución", max_length=30)
    logo = models.ImageField(upload_to='imagenes/', verbose_name="Logo", )
    telefono = models.CharField(verbose_name="Teléfono", max_length=10)
    
    class Meta:
        verbose_name = 'Institución Educativa'
        verbose_name_plural = 'Institución Educativa'

    def __str__(self):
        return f'Dirección: {self.direcion} | correo: {self.email} | institución: {self.nombre_institucion} | telefono: {self.telefono}'

    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()


class Periodo(models.Model):
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")    
    fecha_fin = models.DateField(verbose_name="Fecha de Fin")    
    
    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'

    def __str__(self):
        return f'Inicio: {self.fecha_inicio} | Fin: {self.fecha_fin}'


class Nivel(models.Model):
    nombre_nivel = models.CharField(max_length=15, verbose_name="Nivel")
    
    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'

    def __str__(self):
        return f'Nivel: {self.nombre_nivel}'
    
    
class Grado(models.Model):
    nombre_grado = models.CharField(max_length=1,verbose_name="Grado")
    
    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'

    def __str__(self):
        return f'Grado: {self.nombre_grado}'


class Seccion(models.Model):
    nombre_seccion = models.CharField(max_length=1,verbose_name="Sección")
    
    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'

    def __str__(self):
        return f'Sección: {self.nombre_seccion}'


class Persona(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=45, blank=False, null=False)
    apellido_paterno = models.CharField(verbose_name="Apellido Paterno", max_length=45, blank=False, null=False)
    apellido_materno = models.CharField(verbose_name="Apellido Materno", max_length=45, blank=False, null=False)
    dni = models.CharField(verbose_name="DNI", max_length=8)
    celular = models.CharField(verbose_name="Celular", max_length=9)
    genero = models.CharField(verbose_name="Género", max_length=3)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento" )
    foto = models.ImageField(upload_to='imagenes/', verbose_name="Foto de Perfil", null=True)
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido_paterno} {self.apellido_materno} | DNI: {self.dni}'    
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()


class Docente(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True,verbose_name="ID Persona")
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,verbose_name="ID Usuario")

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        return f'Información: {self.persona} | Usuario: {self.usuario}'


class Alumno(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True,verbose_name="ID Persona")
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,verbose_name="ID Usuario")
    nivel = models.ForeignKey(Nivel, on_delete=models.SET_NULL, null=True,verbose_name="Nivel")
    grado = models.ForeignKey(Grado, on_delete=models.SET_NULL, null=True,verbose_name="Grado")
    seccion = models.ForeignKey(Seccion, on_delete=models.SET_NULL, null=True,verbose_name="Seccion")

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        return f'Información: {self.persona} | nivel: {self.nivel}, {self.grado} {self.seccion}'
    
    
class Curso(models.Model):
    etiqueta = models.CharField(max_length=15, verbose_name="Etiqueta")
    nombre_curso = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True,verbose_name="ID Docente")
    nivel = models.ForeignKey(Nivel, on_delete=models.SET_NULL, null=True,verbose_name="ID Nivel")
    grado = models.ForeignKey(Grado, on_delete=models.SET_NULL, null=True,verbose_name="ID Grado")
    seccion = models.ForeignKey(Seccion, on_delete=models.SET_NULL, null=True,verbose_name="ID Seccion")
    periodo = models.ForeignKey(Periodo, on_delete=models.SET_NULL, null=True,verbose_name="ID Periodo")
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return f'Curso: {self.etiqueta}-{self.nombre_curso} | nivel: {self.nivel}, {self.grado} {self.seccion} | perioro: {self.periodo}'
    

class Detalle_alumno_en_curso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True, verbose_name="ID Alumno")
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, verbose_name="ID Curso")
    
    class Meta:
        verbose_name = 'Detalle de alumno en un curso'
        verbose_name_plural = 'Detalle de alumno en un curso'

    def __str__(self):
        return f'Curso: {self.curso} | Alumno: {self.alumno}'
    
    
class Asistencia(models.Model):
    detalle_alumno_en_curso = models.ForeignKey(Detalle_alumno_en_curso, on_delete=models.SET_NULL, null=True, verbose_name="alumno en curso")
    fecha = models.DateField(verbose_name="Inasistencia")
    
    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        return f'Alumno:{self.detalle_alumno_en_curso.alumno} | fecha de Inasistencia: {self.fecha}'
    

class Contenido(models.Model):
    titulo = models.CharField(max_length=20, verbose_name="Titulo del contenido")
    
    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'

    def __str__(self):
        return f'Titulo del contenido: {self.titulo}'
    

class Carpeta(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, verbose_name="ID Curso")
    contenido = models.ForeignKey(Contenido, on_delete=models.SET_NULL, null=True, verbose_name="ID Contenido")
    nombre_folder = models.CharField(max_length=45, verbose_name="Nombre de la capeta")
    es_tarea = models.BooleanField(default=False, verbose_name="¿Es tarea?")
    tiempo_limite =  models.DateField(verbose_name="Tiempo límite", null=True)

    class Meta:
        verbose_name = 'Carpeta'
        verbose_name_plural = 'Carpetas'

    def __str__(self):
        return f'Curso: {self.curso} | Contenido: {self.contenido} | Carpeta: {self.nombre_folder} | ¿Es tarea ?: {self.es_tarea}'   
    
     
class Archivo(models.Model):
    carpeta =  models.ForeignKey(Carpeta, on_delete=models.SET_NULL, null=True, verbose_name="ID Carpeta")
    nombre_archivo = models.CharField(max_length=45, verbose_name="nombre del archivo")
    ruta_archivo = models.FileField(null=True, verbose_name="Archivo")
    visibilidad_alumno = models.BooleanField(default=False, verbose_name="visibilidad para alumno")
    
    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'

    def __str__(self):
        return f'Carpeta: {self.carpeta} | nombre del archivo: {self.nombre_archivo} | visibilidad para alumnos: {self.visibilidad_alumno}'  
    
    