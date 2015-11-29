from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.backends.db import SessionStore

from decimal import *
import pyboleto
from pyboleto.bank.bancodobrasil import BoletoBB
from pyboleto.data import BoletoData
from pyboleto.pdf import BoletoPDF

import datetime

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
	list_cursos = Curso.objects.all()
	print (list_cursos)
	return render(request, 'curso/lista_cursos.html', {'list_cursos': list_cursos})


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
			mensagem = "O nome ou a senha estão errados"
			return render(request, 'curso/login.html', {'message':mensagem})
		
	return render(request, 'curso/login.html')

def sair(request):
	logout(request)
	return redirect('/')

def confirmar_inscricao(request, id):
	if request.user.is_authenticated():
		aluno = Aluno.objects.get(user_ptr_id=request.session['_auth_user_id'])
	curso = get_object_or_404(Curso, id=id)
	
	return render(request, 'curso/confirmar_inscricao.html', {'curso':curso, 'aluno':aluno})
