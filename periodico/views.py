from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import Professor, Publicacao
from .forms import ProfessorForm, PublicacaoForm, CustomUserCreationForm, FeedbackForm
from django.contrib.auth.decorators import login_required 
from django.db.models import Q,F
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib import messages


def home(request):
  
    query = request.GET.get('q') 
    if query:
        posts_list = Publicacao.objects.filter(Q(titulo__icontains=query) |  Q(professor__nome__icontains=query) ).order_by('-id')
    else:
        posts_list = Publicacao.objects.all().order_by('-id')

    # Define quantos cards por página (ex: 6)
    paginator = Paginator(posts_list, 12) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj, 'query': query, 'total_publicacao': '6500'})

def lista_professores(request):
    professores = Professor.objects.all()
    return render(request, 'lista_professores.html', {'professores': professores})

def detalhe_publicacao(request, pk):
    # 'pk' é a Primary Key (ID) da publicação
    publicacao = get_object_or_404(Publicacao, pk=pk)
    Publicacao.objects.filter(pk=publicacao.id).update(visualizacoes=F('visualizacoes') + 1)  
    # Processamento do Feedback
    if request.method == 'POST' and 'btn_feedback' in request.POST:
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            # Dados do formulário
            nome = feedback_form.cleaned_data['nome']
            email = feedback_form.cleaned_data['email']
            mensagem = feedback_form.cleaned_data['mensagem']
            
            # 3. Envio do E-mail (usando a config do Gmail que fizemos)
            try:
                assunto = f"Feedback sobre: {publicacao.titulo[:50]}"
                corpo = f"O usuário {nome} ({email}) enviou um feedback sobre a publicação '{publicacao.titulo}':\n\n{mensagem}"
                
                send_mail(
                    assunto,
                    corpo,
                    'ronaldo.serra@ifma.edu.br',  # Remetente (seu Gmail config)
                    ['ronaldo.serra@ifma.edu.br'], # Destinatário (você)
                    fail_silently=False,
                )
                messages.success(request, 'Obrigado! Seu feedback foi enviado com sucesso.')
                return redirect('detalhe_publicacao', pk=pk)
            except Exception as e:
                messages.error(request, 'Erro ao enviar e-mail. Tente novamente mais tarde.')
    else:
        feedback_form = FeedbackForm()

    return render(request, 'detalhe.html', {
        'publicacao': publicacao,
        'feedback_form': feedback_form
    })
    return render(request, 'detalhe.html', {'publicacao': publicacao})

@login_required # Somente logados acessam
def cadastrar_publicacao(request):
    if request.method == 'POST':
        form = PublicacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_professores') # Ou para onde desejar
    else:
        form = PublicacaoForm()
    
    return render(request, 'cadastrar_publicacao.html', {'form': form})

@login_required # Somente logados acessam
def cadastrar_professor(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_professores')
    return render(request, 'cadastro_professor.html', {'form': form})

def perfil_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    # Pegamos todas as publicações ligadas a este professor
    publicacoes = professor.publicacoes.all().order_by('-ano')
    return render(request, 'perfil_professor.html', {
        'professor': professor,
        'publicacoes': publicacoes
    })
    
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('login') # Redireciona para o login após sucesso
    else:
        form = CustomUserCreationForm()
    
    return render(request,'cadastro_user.html',  {'form': form})