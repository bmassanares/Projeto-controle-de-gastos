from django.forms import ModelForm
from contas.models import Transacao
#criação de um formulário 
class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']

