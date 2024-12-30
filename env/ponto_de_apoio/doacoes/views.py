from django.shortcuts import render,redirect
from .forms import DoacaoForm
from .models import Doacao
from .models import Contato
from .forms import ContatoForm, ReceberForm

def home(request):    
        return render(request, 'doacoes/index.html')#Tem que colocar doacoes/ nas proximas rotas


def login(request):
    return render(request, 'doacoes/login.html')


def listar_doacao(request):
    doacoes = Doacao.objects.all()
    return render(request, 'doacoes/listar_clientes.html', {'doacoes': doacoes})#Tem que colocar doacoes/ nas proximas rotas


def receber_dados(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            itens_selecionados = ', '.join(
                request.POST.getlist('itens'))  # Captura os valores
            doacao = form.save(commit=False)
            doacao.itens = itens_selecionados
            doacao.save()
    else:
        form = DoacaoForm()
    return render(request, 'doacoes/doar.html', {'form': form})


def receber_doacao(request):
    
    if request.method == 'POST':
        print(request.POST)
        form = ReceberForm(request.POST)
        if form.is_valid():
            # Capturar os checkboxes selecionados
            itens_selecionados = ', '.join(
                request.POST.getlist('itens'))  # Captura os valores
            doacao = form.save(commit=False)
            doacao.itens = itens_selecionados
            doacao.save()
    else:
        form = ReceberForm()
    return render(request, 'doacoes/receba.html')




def contatar(request):
    
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contato')  
     
    else: 
        form = ContatoForm()
        return render(request, 'doacoes/contato.html', {'form': form})


