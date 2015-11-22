from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Aluno(models.Model):
	usuario = models.ForeignKey(User, blank=True, null=False, editable=False, default="")
	
	matricula = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=200)
	endereco = models.CharField(max_length=400)
	data_de_nascimento = models.DateField(blank=True, null=False)
	data_de_matricula = models.DateTimeField(blank=True, null=True)
	ativo = models.BooleanField(default=False)
	email = models.EmailField()
	senha = models.CharField(max_length=20, null=True)
	

	class Meta:
		verbose_name = "Aluno"
		verbose_name_plural = "Alunos"

	def save(self):
		if not self.matricula:
			c = Aluno.objects.filter(email=self.email).count()
			if c:
				print("Email não existe")
			usr = User.objects.filter(username=self.email)
			if usr:
				u = usr[0]
			else:
				u = User.objects.create_user(self.email, self.email, self.senha)
			u.save()
			self.usuario = u
		else:
			self.usuario.username = self.email
			self.usuario.email = self.email
			self.usuario.set_password(self.senha)

		super(Aluno, self).save()


	def publish(self):
		self.data_de_matricula = timezone.now()
		self.save()

	def __str__(self):
		return self.nome


class Professor(models.Model):
	usuario = models.ForeignKey(User, blank=True, null=True, editable=False, default="")

	nome = models.CharField(max_length=200)
	
	cpf = models.IntegerField()
	endereco = models.CharField(max_length=400)
	data_de_nascimento = models.DateField(blank=True, null=False)
	email = models.EmailField()
	senha = models.CharField(max_length=20, null=True)
	
	class Meta:
		verbose_name = "Professor"
		verbose_name_plural = "Professores"

	def save(self):
		if not self.id:
			c = Professor.objects.filter(email=self.email).count()
			if c:
				print("Email não existe")
			usr = User.objects.filter(username=self.email)
			if usr:
				p = usr[0]
			else:
				p = User.objects.create_user(self.email, self.email, self.senha)
			p.save()
			self.professor = p
		else:
			self.professor.username = self.email
			self.professor.email = self.email
			self.professor.set_password(self.senha)
		super(Professor, self).save()

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome


class Curso(models.Model):

	nome = models.CharField(max_length=200)
	disciplinas = models.ManyToManyField('Disciplina')
	alunos = models.ManyToManyField('Aluno')

	class Meta:
		verbose_name = "Curso"
		verbose_name_plural = "Cursos"

	def publish(self):
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
