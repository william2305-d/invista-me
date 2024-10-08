from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required


def pagina_inicial(request):
    return HttpResponse("Pronto para investir!")

def pagina_contato(request):
    return HttpResponse("(31) 993173589")

def minha_historia(request):
        pessoa = {
            'nome': 'Jeff',
            'idade': 28,
            'hobby': 'Games'
        }
        return render(request,'investimentos/minha_historia.html', pessoa)

def novo_investimento(request):
    return render(request,'investimentos/novo_investimento.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request,'investimentos/investimento_registrado.html', investimento)

def investimentos(request):
    dados = {
        'dados':Investimento.objects.all()
    }
    return render(request,'investimentos/exibir_investimento.html', context=dados)

@login_required
def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request,'investimentos/detalhe.html', dados)

@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)

@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    # novo_investimento/1 -> GET
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    elif request.method == 'POST':
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')

@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    else:
        return render(request,'investimentos/confirmar_exclusao.html')


# Create your views here.
