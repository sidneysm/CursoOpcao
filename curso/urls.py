from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^realizamatricula$', views.realiza_matricula),
	url(r'^buscar_aluno$', views.buscar_aluno),
	url(r'^lista_alunos$', views.lista_alunos),
	url(r'^curso$', views.curso),
	url(r'^login$', views.login),
]