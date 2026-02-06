from .models import Publicacao

def estatisticas_globais(request):
    # Retorna um dicionário com os dados que você quer em todas as telas
    return {
        'total_geral_publicacoes': Publicacao.objects.count()
    }