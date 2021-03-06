from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^realizamatricula$', views.realiza_matricula),
	url(r'^cursos$', views.cursos),
	url(r'^aluno$', views.aluno),
	url(r'^professor$', views.professor),
	url(r'^fazer_login$', views.fazer_login),
	url(r'^aluno/editar$', views.editar_aluno),
	url(r'^sair$', views.sair),
	url(r'^aluno/(?P<id>[0-9]+)/confirmar_inscricao/$', views.confirmar_inscricao, name="confirmar_inscricao"),
	url(r'^gerar_boleto/(?P<id_curso>[0-9]+)/$$', views.gerar_boleto)
]