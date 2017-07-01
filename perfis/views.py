from django.shortcuts import render
from perfis.models import Perfil
 
def index(request):
	return render(request, 'index.html')

def exibir(request, perfil_id):

	perfil = Perfil()

	if perfil_id == '1':
		perfil = Perfil('Eu mesmo', 'lindo_eusei@email.com', '123456', 'Empresinha')

	return render(request, 'perfil.html', {"perfil" : perfil})