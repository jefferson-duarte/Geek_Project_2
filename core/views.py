from django.shortcuts import render

from core.models import Produto
from .forms import ContatoForm, ProdutoModelForm, Produto
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'produtos': Produto.objects.all(),
    }
    
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
           form.send_mail()
           
           messages.success(request, 'E-mail enviado com sucesso.')
           form = ContatoForm()
        else:
            messages.error(request, 'Erro no envio do e-mail.')
            
    context = {
        'form': form,
    }
    return render(request, 'contato.html', context)

@login_required(login_url='/')
def produto(request):
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Produto salvo com sucesso!')
            form = ProdutoModelForm()
        
        else:
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = ProdutoModelForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'produto.html', context)
