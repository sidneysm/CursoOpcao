from django.shortcuts import render
from .forms import AlunoForms
from .models import *

# Create your views here.
def index(request):
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
	else:
		form = AlunoForms
	return render(request, 'curso/realiza_matricula.html', {'form': form})

def lista_alunos(request):
	alunos = Aluno.objects.filter(nome__contains=request.POST['nome'])
	return render(request, 'curso/lista_aluno.html', {'alunos':alunos})
