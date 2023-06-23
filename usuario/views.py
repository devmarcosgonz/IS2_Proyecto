from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuarios
from .forms import UsuariosForm

# Create your views here.

def lista_usuarios(request):
    usuarios = Usuarios.objects.all().order_by('id_usuario')
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})


# def usuarios_detail(request, pk):
#     usuario = get_object_or_404(Usuarios, pk=pk)
#     return render(request, 'usuarios/usuarios_detail.html', {'usuario': usuario})


def crear_usuario(request):
    if request.method == "POST":
        form = UsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            return redirect('usuario:listausuarios')
    else:
        form = UsuariosForm()
    return render(request, 'crear_usuario.html', {'form': form})


def actualizar_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == "POST":
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            return redirect('usuario:listausuarios')
    else:
        form = UsuariosForm(instance=usuario)
    return render(request, 'actualizar_usuario.html', {'form': form})


def eliminar_usuario(request, pk):
    print(request, pk)
    usuario = get_object_or_404(Usuarios, pk=pk)
    usuario.is_active = False  # Cambiar el estado a Inactivo
    usuario.save()
    return redirect('usuario:listausuarios')
