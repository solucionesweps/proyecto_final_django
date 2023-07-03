from django.contrib import admin
from .models import Categoria
from .models import Gestion
from .models import GrupoEntrenamiento
from .models import Persona
from .models import Inscripcion


# Register your models here.
#Categorias

class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre_categoria','estado_categoria')
    list_filter=('nombre_categoria','estado_categoria')
    search_fields=('nombre_categoria','estado_categoria')
    ordering=('nombre_categoria','estado_categoria')

admin.site.register(Categoria, CategoriaAdmin)

"""
Gestion
"""
class GestionAdmin(admin.ModelAdmin):
    list_display=('nombre_gestion','estado_gestion')
    list_filter=('nombre_gestion','estado_gestion')
    search_fields=('nombre_gestion','estado_gestion')
    ordering=('nombre_gestion','estado_gestion')

admin.site.register(Gestion, GestionAdmin)

"""
Grupo Entrenamiento
"""
class EntrenamientoAdmin(admin.ModelAdmin):
    list_display=('nombre_grupo','hora_inicio','hora_fin','id_categoria_id','id_gestion','id_persona_entrenador_id','estado_grupo')
    list_filter=('nombre_grupo','hora_inicio','hora_fin','estado_grupo')
    search_fields=('nombre_grupo','hora_inicio','hora_fin','estado_grupo')
    ordering=('nombre_grupo','hora_inicio','hora_fin','estado_grupo')

admin.site.register(GrupoEntrenamiento, EntrenamientoAdmin)

"""
Persona
"""
""
class PersonaAdmin(admin.ModelAdmin):
    list_display=('ci','nombre','paterno','materno','fecha_nacimiento','genero','celular')
    list_filter=('nombre','genero')
    search_fields=('ci','nombre','paterno','materno','fecha_nacimiento','genero','celular')
    ordering=('ci','nombre','paterno','materno','fecha_nacimiento','genero','celular')


admin.site.register(Persona, PersonaAdmin)

"""
Inscripción
"""
class InscripcionAdmin(admin.ModelAdmin):
    list_display=('id_inscripcion','fecha_inicio','fecha_fin','id_persona_estudiante_id','id_grupo_entrenamiento_id','estado_inscripcion')
    list_filter=('fecha_inicio','fecha_fin')
    search_fields=('id_inscripcion','fecha_inicio','fecha_fin','id_persona_estudiante_id','id_grupo_entrenamiento_id','estado_inscripcion')
    ordering=('id_inscripcion','fecha_inicio','fecha_fin','id_persona_estudiante_id','id_grupo_entrenamiento_id','estado_inscripcion')

admin.site.register(Inscripcion, InscripcionAdmin)