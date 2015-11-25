from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class AlunoForms(UserCreationForm):
	
	class Meta:
		model = Aluno
		fields = ('username', 'first_name', 'last_name', 'endereco', 'data_de_nascimento', 'email', )