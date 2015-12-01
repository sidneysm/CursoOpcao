from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse, FileResponse


from decimal import *
import pyboleto
from pyboleto.bank.bancodobrasil import BoletoBB
from pyboleto.data import BoletoData
from pyboleto.pdf import BoletoPDF

import datetime
from curso.util import print_all, print_bb
from .forms import AlunoForms, AtualizaAlunoForms
from .models import *

# Create your views here.


def index(request):
	"""
	Redireciona para a página inicial
	"""
	
	return render(request, 'curso/index.html')


def cursos(request):
	"""
	Exibe todos os cursos para o aluno escolher no qual matricular-se.
	"""
	list_cursos = Curso.objects.all()
	print (list_cursos)
	return render(request, 'curso/lista_cursos.html', {'list_cursos': list_cursos})


def realiza_matricula(request):
	"""
		Exibe o formulario de cadastro e salva o aluno como um usuário do sistema.
		Abre a a tela de login apos o cadastro.
	"""
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

def aluno(request):
	"""
	Entra na tela de login do aluno.
	Uma vez logado o aluno é autenticado abrindo assim uma sessão para ele.
	Uma vez logado essa view direciona o usuário para uma página com seus dados. 

	"""
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

def editar_aluno(request):
	"""
	Possibilita o aluno alterar os seus dados cadastrados.
	Uma vez alterado o aluno precisa relogar-se no sistema.
	"""

	aluno = Aluno.objects.get(user_ptr_id=request.session['_auth_user_id'])
	if request.method == "POST":


		form = AtualizaAlunoForms(data=request.POST, instance=aluno)
		if form.is_valid():
			aluno = form.save(commit=False)
			aluno.save()
			index(request)
			return render(request, 'curso/login.html',)
	else:
		print(type(aluno))
		form = AtualizaAlunoForms(instance=aluno)
	return render(request, 'curso/editar_aluno.html', {'form': form})
	


def sair(request):
	"""
	Realiza o logout do aluno e direciona o sistema para a página inicial.
	"""
	logout(request)
	return redirect('/')

def confirmar_inscricao(request, id):
	"""
	Mostra uma página com informações do aluno e do curso escolhido para a matrícula.
	"""
	aluno = Aluno.objects.get(user_ptr_id=request.session['_auth_user_id'])
	curso = get_object_or_404(Curso, id=id)
	
	return render(request, 'curso/confirmar_inscricao.html', {'curso':curso, 'aluno':aluno})

def gerar_boleto(request, id_curso):
	"""
	Gera uma boleto com os dados da empresa do curso e do aluno. 
	O valor dos cursos são fixos.
	"""
	aluno = Aluno.objects.get(user_ptr_id=request.session['_auth_user_id'])
	aluno.situacao = "Aguardando Confirmação de Pagamento"
	aluno.save()
	curso = Curso.objects.get(id=id_curso)
	curso.alunos.add(aluno)
	curso.save()
	if request.user.is_authenticated():
		
		print_bb(aluno)
		file_path ='curso/boletos/boleto-teste-%s.pdf' % aluno.first_name
		
		if request.method == "GET":
			fp = open(file_path, 'rb')
			response = HttpResponse(fp.read())
			fp.close()

			response['Content-Disposition'] = 'attachment; filename=%s' % 'boleto-teste-%s.pdf' % aluno.first_name
		
	return response



		