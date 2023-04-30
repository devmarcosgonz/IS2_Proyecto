from django.shortcuts import render, get_object_or_404
from .models import Sprints
from .forms import SprintForm

# Create your views here.

def lista_sprints(request):
    sprints = Sprints.objects.all().order_by('id_sprint')
    return render(request, 'lista_sprints.html', {'sprints': sprints})

# def usuarios_detail(request, pk):
#     usuario = get_object_or_404(Usuarios, pk=pk)
#     return render(request, 'usuarios/usuarios_detail.html', {'usuario': usuario})


def crear_sprint(request):
    if request.method == "POST":
        form = SprintForm(request.POST)
        if form.is_valid():
            sprint = form.save(commit=False)
            sprint.save()
            sprints = Sprints.objects.all().order_by('id_sprint')
            return render(request, 'lista_sprints.html', {'sprints': sprints})
    else:
        form = SprintForm()
    return render(request, 'crear_sprint.html', {'form': form})


def actualizar_sprint(request, pk):
    proyecto = get_object_or_404(Sprints, pk=pk)
    if request.method == "POST":
        form = SprintForm(request.POST, instance=sprint)
        if form.is_valid():
            sprint = form.save(commit=False)
            sprint.save()
            sprints = Sprints.objects.all().order_by('id_sprint')
            return render(request, 'lista_sprints.html', {'sprints': sprints})
    else:
        form = SprintForm(instance=sprint)
    return render(request, 'actualizar_sprint.html', {'form': form})


def eliminar_sprint(request, pk):
    print(request, pk)
    sprint = get_object_or_404(Sprints, pk=pk)
    sprint.delete()
    sprints = Sprints.objects.all().order_by('id_sprint')
    return render(request, 'lista_sprints.html', {'sprints': sprints})
