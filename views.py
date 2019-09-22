from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from contas.models import Transacao
from .form import TransacaoForm
'''
#trecho de código que vamos escrever que vai executar aquela página que o usuário quer abrir 
# Create your views here.
def home(request):
    now = datetime.datetime.now()
    html = "<html><body> It's now %s.</body></html>" % now
    return HttpResponse(html)
# com esse código escrito acima, quando abrimos a path que contém a função "home"
# classe que passamos para a url que, assim que o django resolver essa "url" (url resolution), a função "home" 
# será chamada e faz o que tem que fazer, devolvendo uma response 
# (ou seja, o que tem dentro dessa função, executando-a).
'''
def home(request):
    data={}
    data['transacao'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    #html = "<html><body> It's now %s.</body></html>" % now
    return render(request, 'contas/home.htm', data)
    #como estamos usando o render, temos que colocar essa request de volta

def listagem(request):
    data={}
    data['transacoes'] = Transacao.objects.all()
    #aqui estamos pegando todas as transações do banco e colocamos tudo dentro da variável "data", dentro de transacoes. 
                        #nome do model.esse objects é o manager 
                        # manager = classe que o django implementa para todos os models, quando criamos um model com o models.Model 
                        # ele já vem com um manager padrão, trazendo operações de banco de dados para nós
                        # como: all ( o qual busca todos os dados do banco), filter (que vai buscar através de uma filtragem 
                        # vai passar os parametros para filtrar), last (pega a ultima transacão do banco), first (pega a primeira) do django 
                        #assim estamos chamando todos os objetos do model Transacao
    return render(request, 'contas/listagem.htm', data)

def nova_transacao(request):
    data = {}
    #definição de um dicionário chamado "data"
    form = TransacaoForm(request.POST or None)
    #estamos criando um novo form, que vai utilizar o formulário com as fields listadas lá no form (no caso: TransacaoForm)
    #esse request o django vai procurar se tem no form algo preenchido, se tiver, ele vai criar um form preenchido 
    #em seguida estamos validando o form para poder salvar no banco
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
        #mando ele direto para a listagem, caso não for válido ele vai colocar o form dentro da data e vai mandar novamente 
        #para a minha view
    data['form'] = form
    #dentro do dicionário estamos colocando o form que foi criado 
    return render(request, 'contas/form.htm', data)
    #return = estamos mandando o formulário criado para a tela

def update (request, pk):
    #quando a gente faz o request, o que estamos passando na url é a pk, então a update recebe um parametro a mais, que é o pk (primary key)
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    #estamos criando um objeto chamado transacao que recebe o model Transacao e nele vamos usar o manage do django, no caso vamos usar o get, o qual retorna apenas um objeto para nós, 
    #se usassemos o filter, iria ser retornado vários objetos
    #estamos pegando a transacao do banco pela pk, então pk recebe pk, localizando essa transacao no banco criando um objeto chamado transacao

    form = TransacaoForm(request.POST or None, instance=transacao)
    #estamos instanciando um form, aquele que fizemos no form.py, porém agora podemos passar um atributo "instance" que, no nosso caso, é a transacao 
    #então não vamos começar um form vazio jamais, ou eu começo um que o usuário está passando para mim, ou eu inicio através da instância
    #de um objeto que eu acabei de pegar no banco 
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
        #salvei o form e redirecionei, se não for válido eu pego o form 

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.htm', data)

def delete(request, pk):
    # a gente passa o id do objeto que será deletado, localiza ele no banco, deleta e redireciona
     transacao = Transacao.objects.get(pk=pk)
     transacao.delete()
     return redirect('url_listagem')

