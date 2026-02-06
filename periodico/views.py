from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Publicacao

def home(request):
    query = request.GET.get('q')
    
    if query:
        posts_list = Publicacao.objects.filter(titulo__icontains=query).order_by('-id')
    else:
        posts_list = Publicacao.objects.all().order_by('-id')

    # Define quantos cards por página (ex: 6)
    paginator = Paginator(posts_list, 6) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj, 'query': query})

from django.shortcuts import render, get_object_or_404
from .models import Publicacao

def detalhe_publicacao(request, pk):
    # 'pk' é a Primary Key (ID) da publicação
    publicacao = get_object_or_404(Publicacao, pk=pk)
    return render(request, 'detalhe.html', {'publicacao': publicacao})
