from django.shortcuts import render
from django.contrib.auth import authenticate
from .forms import AlunoForms
from .models import *

# Create your views here.
def index(request):
	if request.method == "POST":
		print("Aluno invalido")
	return render(request, 'curso/index.html')

def buscar_aluno(request):
	return render(request, 'curso/buscar_aluno.html')

def curso(request):
	return render(request, 'curso/curso.html')

def realiza_matricula(request):
	if request.method == "POST":
		form = AlunoForms(request.POST)
		if form.is_valid():
			aluno = form.save(commit=False)
			aluno.save()
			index(request)
	else:
		form = AlunoForms
	return render(request, 'curso/realiza_cadastro.html', {'form': form})

def lista_alunos(request):
	alunos = Aluno.objects.filter(nome__contains=request.POST['nome'])
	return render(request, 'curso/lista_aluno.html', {'alunos':alunos})

def login(request):
	if request.method == "POST":
		print (request.POST['nome'])
		usuario = authenticate(username=request.POST['nome'], password=request.POST['senha'])
		print(request.POST)
		if usuario is not None:
			if usuario.is_active:
			    print("User is valid, active and authenticated")
			    print (type(usuario))
			    return render(request, 'curso/aluno_detalhes.html')
			else:
			    print("The password is valid, but the account has been disabled!")
		else:
		    # the authentication system was unable to verify the username and password
		    print("The username and password were incorrect.")
		
	return render(request, 'curso/index.html')

def usuario_detalhe(request):
	return render(request, 'curso/aluno_detalhes.html')