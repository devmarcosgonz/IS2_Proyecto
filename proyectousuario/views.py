from django.shortcuts import render, redirect, get_object_or_404
from .models import ProyectoUsuario
from .forms import ProyectoUsuarioForm

# Create your views here.

def lista_proyectousuarios(request):
    proyectousuarios = ProyectoUsuario.objects.all().order_by('id_proyecto_usuario')
    return render(request, 'lista_proyectousuarios.html', {'proyectousuarios': proyectousuarios})


# def usuarios_detail(request, pk):
#     usuario = get_object_or_404(Usuarios, pk=pk)
#     return render(request, 'usuarios/usuarios_detail.html', {'usuario': usuario})


def crear_proyectousuario(request):
    if request.method == "POST":
        form = ProyectoUsuarioForm(request.POST)
        if form.is_valid():
            proyectousuario = form.save(commit=False)
            proyectousuario.save()
            return redirect('proyectousuario:listaproyectousuarios')
    else:
        form = ProyectoUsuarioForm()
    return render(request, 'crear_proyectousuario.html', {'form': form})


def actualizar_proyectousuario(request, pk):
    proyectousuario = get_object_or_404(ProyectoUsuario, pk=pk)
    if request.method == "POST":
        form = ProyectoUsuarioForm(request.POST, instance=proyectousuario)
        if form.is_valid():
            proyectousuario = form.save(commit=False)
            proyectousuario.save()
            return redirect('proyectousuario:listaproyectousuarios')
    else:
        form = ProyectoUsuarioForm(instance=proyectousuario)
    return render(request, 'actualizar_proyectousuario.html', {'form': form})


def eliminar_proyectousuario(request, pk):
    print(request, pk)
    proyectousuario = get_object_or_404(ProyectoUsuario, pk=pk)
    proyectousuario.delete()
    return redirect('proyectousuario:listaproyectousuarios')