from django.shortcuts import render, get_object_or_404
from .models import Proyectos
from .forms import ProyectosForm

# Create your views here.

def lista_proyectos(request):
    proyectos = Proyectos.objects.all().order_by('id_proyecto')
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

# def usuarios_detail(request, pk):
#     usuario = get_object_or_404(Usuarios, pk=pk)
#     return render(request, 'usuarios/usuarios_detail.html', {'usuario': usuario})


def crear_proyecto(request):
    if request.method == "POST":
        form = ProyectosForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.save()
            proyectos = Proyectos.objects.all().order_by('id_proyecto')
            return render(request, 'lista_proyectos.html', {'proyectos': proyectos})
    else:
        form = ProyectosForm()
    return render(request, 'crear_proyecto.html', {'form': form})


def actualizar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyectos, pk=pk)
    if request.method == "POST":
        form = ProyectosForm(request.POST, instance=proyecto)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.save()
            proyectos = Proyectos.objects.all().order_by('id_proyecto')
            return render(request, 'lista_proyectos.html', {'proyectos': proyectos})
    else:
        form = ProyectosForm(instance=proyecto)
    return render(request, 'actualizar_proyecto.html', {'form': form})


def eliminar_proyecto(request, pk):
    print(request, pk)
    proyecto = get_object_or_404(Proyectos, pk=pk)
    proyecto.delete()
    proyectos = Proyectos.objects.all().order_by('id_proyecto')
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})
