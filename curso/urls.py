from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^realizamatricula$', views.realiza_matricula),
	url(r'^buscar_aluno$', views.buscar_aluno),
	url(r'^lista_alunos$', views.lista_alunos),
	url(r'^cursos$', views.cursos),
	url(r'^aluno$', views.aluno),
	url(r'^sair$', views.sair),
	url(r'confirmar_inscricao/(?P<id>[0-9]+)/$', views.confirmar_inscricao, name="confirmar_inscricao"),
	url(r'^gerar_boleto/(?P<id_curso>[0-9]+)/$$', views.gerar_boleto)
]