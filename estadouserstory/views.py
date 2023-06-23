from django.shortcuts import render, redirect, get_object_or_404
from .models import EstadosUserStory
from .forms import EstadosUserStoryForm

# Create your views here.

def lista_estadouserstories(request):
    estadouserstories = EstadosUserStory.objects.all().order_by('id_estado')
    return render(request, 'lista_estadouserstories.html', {'estadouserstories': estadouserstories})


# def usuarios_detail(request, pk):
#     usuario = get_object_or_404(Usuarios, pk=pk)
#     return render(request, 'usuarios/usuarios_detail.html', {'usuario': usuario})


def crear_estadouserstory(request):
    if request.method == "POST":
        form = EstadosUserStoryForm(request.POST)
        if form.is_valid():
            estadouserstory = form.save(commit=False)
            estadouserstory.save()
            return redirect('estadouserstory:listaestadouserstories')
    else:
        form = EstadosUserStoryForm()
    return render(request, 'crear_estadouserstory.html', {'form': form})


def actualizar_estadouserstory(request, pk):
    estadouserstory = get_object_or_404(EstadosUserStory, pk=pk)
    if request.method == "POST":
        form = EstadosUserStoryForm(request.POST, instance=estadouserstory)
        if form.is_valid():
            estadouserstory = form.save(commit=False)
            estadouserstory.save()
            return redirect('estadouserstory:listaestadouserstories')
    else:
        form = EstadosUserStoryForm(instance=estadouserstory)
    return render(request, 'actualizar_estadouserstory.html', {'form': form})


def eliminar_estadouserstory(request, pk):
    print(request, pk)
    estadouserstory = get_object_or_404(EstadosUserStory, pk=pk)
    estadouserstory.delete()
    return redirect('estadouserstory:listaestadouserstories')
