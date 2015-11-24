from django.contrib import admin
from .models import *
# Register your models here.

modelos = [
	Aluno, 
	Professor, 
	Curso, 
	Disciplina
]
admin.site.register(modelos)