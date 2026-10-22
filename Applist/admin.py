from django.contrib import admin

# Register your models here.
from .models import Proyecto
from .models import Tarea

admin.site.register(Proyecto)
admin.site.register(Tarea)