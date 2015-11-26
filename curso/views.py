from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.backends.db import SessionStore

from .forms import AlunoForms
from .models import *

# Create your views here.


def index(request):
	# if request.user.is_authenticated():
	# 	logout(request)
	return render(request, 'curso/index.html')


def buscar_aluno(request):
	return render(request, 'curso/buscar_aluno.html')


def cursos(request):
	cursos = Curso.objects.all()
	return render(request, 'curso/curso.html', {'cursos': cursos})


def realiza_matricula(request):
	if request.method == "POST":
		form = AlunoForms(request.POST)
		if form.is_valid():
			aluno = form.save(commit=False)
			aluno.save()
			index(request)
			return render(request, 'curso/login.html')
	else:
		form = AlunoForms
	return render(request, 'curso/cadastrar.html', {'form': form})


def lista_alunos(request):
	alunos = Aluno.objects.all()
	return render(request, 'curso/lista_aluno.html', {'alunos': alunos})


def aluno(request):

	if request.user.is_authenticated():
		aluno = Aluno.objects.get(user_ptr_id=request.session['_auth_user_id'])

		return render(request, 'curso/aluno_detalhes.html', {'aluno': aluno},)

	if request.method == "POST":
		print (request.POST['nome'])
		usuario = authenticate(
			username=request.POST['nome'], password=request.POST['senha'])
		
		if usuario is not None:
			if usuario.is_active:
				login(request, usuario)
				aluno = Aluno.objects.get(user_ptr_id=request.session['_auth_user_id'])
				print("User is valid, active and authenticated")
				return render(request, 'curso/aluno_detalhes.html', {'aluno': aluno},)
			else:
				print("The password is valid, but the account has been disabled!")
		else:
			# the authentication system was unable to verify the username and password
			print("The username and password were incorrect.")
		
	return render(request, 'curso/login.html')

def sair(request):
	logout(request)
	return redirect('/')


