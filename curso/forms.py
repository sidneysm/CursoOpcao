from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from curso.util import CPF

class AlunoForms(UserCreationForm):
	"""
	Gera e valida os fomulário para cadastro de um novo aluno
	"""
	class Meta:
		model = Aluno
		
		fields = ('username', 'first_name', 'last_name', 'cpf','endereco', 'data_de_nascimento', 'email', )

	def clean_cpf(self):
		cd = self.cleaned_data
		cpf = cd.get('cpf')
		
		cpf_vaol = CPF(cpf)

		if not cpf_vaol.isValid():
			raise forms.ValidationError("CPF inválido")
		return cpf_vaol

class AtualizaAlunoForms(UserCreationForm):
	"""
	Gera e valida os fomulário para alteração de um aluno existente
	"""
	class Meta:
		model = Aluno
		fields = ('first_name', 'last_name', 'cpf','endereco', 'data_de_nascimento', 'email')
		

	def clean_cpf(self):
		cd = self.cleaned_data
		cpf = cd.get('cpf')
		
		cpf_vaol = CPF(cpf)

		if not cpf_vaol.isValid():
			raise forms.ValidationError("CPF inválido")
		return cpf_vaol

	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		# This is done here, rather than on the field, because the field does 
		# not have access to the initial value
		return self.initial["password"]