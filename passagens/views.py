from django.shortcuts import render
from passagens.forms import PassagensForms

# Create your views here.
def index(request):
    """Formulário"""
    form = PassagensForms()
    contexto = { 'form':form }
    return render(request, 'index.html', contexto)



def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagensForms(request.POST)
        if form.is_valid():
            contexto ={'form':form}
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('form invalido')
            contexto = { 'form':form }
            return render(request, 'index.html', contexto)