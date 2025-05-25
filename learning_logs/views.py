from django.shortcuts import render

from .models import Topic, Entry

from django.shortcuts import render, get_object_or_404


# Importes importantes na submissão de formulário Django em Python
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect, Http404



from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
	"""A página inicial de Learning Log"""
	return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Mostra todos os assuntos."""
    topics = Topic.objects.order_by('date_add')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)

    # Garante que o assunto pertence ao usuário atual
    #if topic.owner != request.user:
    #    raise Http404

    topic = check_topic_owner(request, topic_id)  # Chamada simples

    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')  # Redireciona APENAS se for válido
    
    # Renderiza o formulário (tanto para GET quanto para POST inválido)
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto em particular."""
    topic = get_object_or_404(Topic, id=topic_id, owner=request.user)  # Verifica permissão

    #topic = Topic.objects.filter(owner=request.user).order_by('date_add')
    
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    else:
        form = EntryForm()
    
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic


    #if topic.owner != request.user:
        #raise Http404
    topic = check_topic_owner(request, topic.id)  # Chamada simples


    if request.method != 'POST':   
        # Requisição inicial; preenche previamente o formulário com a entrada atual
        form = EntryForm(instance=entry)
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)



def check_topic_owner(request, topic_id):
    """
    Verifica se o usuário é dono do tópico
    Retorna o tópico se for dono, caso contrário levanta Http404
    """
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404("Tópico não encontrado ou você não tem permissão")
    return topic


