from django.shortcuts import render
from .forms import AlunoForms

# Create your views here.
def index(request):
	return render(request, 'curso/index.html')

def realiza_matricula(request):
	if request.method == "POST":
		form = AlunoForms(request.POST)
		if form.is_valid():
			aluno = form.save(commit=False)
			aluno.save()
	else:
		form = AlunoForms
	return render(request, 'curso/realiza_matricula.html', {'form': form})