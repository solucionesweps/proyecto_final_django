from django.db import models
# Create your models here.

class Estados(models.TextChoices):
    Actual='Activo','Activo'
    Baja='Inactivo','Inactivo'

class Generos(models.TextChoices):
    Masculino='M','Masculino'
    Femenino='F','Femenino'

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=60, null=True, default=None)
    estado_categoria = models.CharField(max_length=10, choices=Estados.choices,default=Estados.Actual)
    def __str__(self):
        return self.nombre_categoria


class Gestion(models.Model):
    id_gestion = models.IntegerField(primary_key=True)
    nombre_gestion = models.CharField(max_length=45, null=True, default=None)
    estado_gestion = models.CharField(max_length=10, choices=Estados.choices,default=Estados.Actual)
    def __str__(self):
        return self.nombre_gestion

class Persona(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    ci = models.CharField(max_length=45, null=True, default=None)
    nombre = models.CharField(max_length=45, null=True, default=None)
    paterno = models.CharField(max_length=45, null=True, default=None)
    materno = models.CharField(max_length=45, null=True, default=None)
    fecha_nacimiento = models.DateField(null=True, default=None)
    genero = models.CharField(max_length=10, choices=Generos.choices,default=Generos.Masculino)
    celular = models.IntegerField(null=True, default=None)
    estado_persona = models.CharField(max_length=10, choices=Estados.choices,default=Estados.Actual)


class GrupoEntrenamiento(models.Model):
    id_grupo_entrenamiento = models.IntegerField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE)
    id_persona_entrenador = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre_grupo = models.CharField(max_length=45, null=True, default=None)
    hora_inicio = models.TimeField(null=True, default=None)
    hora_fin = models.TimeField(null=True, default=None)
    estado_grupo = models.CharField(max_length=10, choices=Estados.choices,default=Estados.Actual)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)



class Inscripcion(models.Model):
    id_inscripcion = models.IntegerField(primary_key=True)
    id_grupo_entrenamiento = models.ForeignKey(GrupoEntrenamiento, on_delete=models.CASCADE)
    id_persona_estudiante = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=True, default=None)
    fecha_fin = models.DateField(null=True, default=None)
    estado_inscripcion = models.CharField(max_length=10, choices=Estados.choices,default=Estados.Actual)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

