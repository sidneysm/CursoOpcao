from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Aluno(models.Model):
	usuario = models.OneToOneField(User, blank=True, null=False, editable=False, default="")
	endereco = models.CharField(max_length=400)
	data_de_nascimento = models.DateField(blank=True, null=False)
	data_de_matricula = models.DateTimeField(blank=True, null=True)
	ativo = models.BooleanField()
	email = models.EmailField()
	senha = models.CharField(max_length=20)
	

	class Meta:
		verbose_name = "Aluno"
		verbose_name_plural = "Alunos"

	def publish(self):
		self.data_de_matricula = timezone.now()
		self.save()

	def __str__(self):
		return self.nome


class Professor(models.Model):
	nome = models.CharField(max_length=200)
	cpf = models.IntegerField()
	endereco = models.CharField(max_length=400)
	data_de_nascimento = models.DateField(blank=True, null=False)
	email = models.EmailField()
	
	
	class Meta:
		verbose_name = "Professor"
		verbose_name_plural = "Professor"

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome


class Curso(models.Model):

	nome = models.CharField(max_length=200)
	disciplinas = models.ManyToManyField('Disciplina')
	alunos = models.ManyToManyField('Aluno', null=True, default="")

	class Meta:
		verbose_name = "Curso"
		verbose_name_plural = "Cursos"

	def publish(self):
		for aluno in self.alunos:
			aluno.ativo = True
			
		self.save()

	def __str__(self):
		return self.nome


class Disciplina(models.Model):

	nome = models.CharField(max_length=60)
	Professor = models.ManyToManyField('Professor')

	class Meta:
		verbose_name = "Disciplina"
		verbose_name_plural = "Disciplinas"

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome
