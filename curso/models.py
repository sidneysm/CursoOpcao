from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from curso.util import CPF

from curso.enums import Situacao

# Create your models here.


class Aluno(User):

	cpf = models.CharField(max_length=14)
	endereco = models.CharField(max_length=400)
	data_de_nascimento = models.DateField(blank=True, null=False)
	data_de_matricula = models.DateTimeField(blank=True, null=True)
	telefone = models.CharField(max_length=20)
	situacao = models.CharField(max_length=50, default=Situacao.nao_pago.value)

	class Meta:
		verbose_name = "Aluno"
		verbose_name_plural = "Alunos"

	def __str__(self):
		return self.first_name


class Professor(User):	
	cpf = models.CharField(max_length=14)
	endereco = models.CharField(max_length=400)
	data_de_nascimento = models.DateField(blank=True, null=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.first_name


class Curso(models.Model):

	nome = models.CharField(max_length=200)
	descricao = models.TextField(null=True)
	disciplinas = models.ManyToManyField('Disciplina')
	alunos = models.ManyToManyField('Aluno', blank=True,)
	duracao = models.IntegerField(null=True)
	data_de_inicio = models.DateField(null=True)


	class Meta:
		verbose_name = "Curso"
		verbose_name_plural = "Cursos"

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome


class Disciplina(models.Model):

	nome = models.CharField(max_length=60)
	professores = models.ManyToManyField('Professor')

	class Meta:
		verbose_name = "Disciplina"
		verbose_name_plural = "Disciplinas"

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome
