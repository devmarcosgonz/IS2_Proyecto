from django.shortcuts import render, redirect, get_object_or_404
from .models import Roles
from .forms import RolesForm

# Create your views here.

def lista_roles(request):
    roles = Roles.objects.all().order_by('id_rol')
    return render(request, 'lista_roles.html', {'roles': roles})

# def usuarios_detail(request, pk):
#     usuario = get_object_or_404(Usuarios, pk=pk)
#     return render(request, 'usuarios/usuarios_detail.html', {'usuario': usuario})


def crear_rol(request):
    if request.method == "POST":
        form = RolesForm(request.POST)
        if form.is_valid():
            rol = form.save(commit=False)
            rol.save()
            return redirect('rol:listaroles')
    else:
        form = RolesForm()
    return render(request, 'crear_rol.html', {'form': form})


def actualizar_rol(request, pk):
    rol = get_object_or_404(Roles, pk=pk)
    if request.method == "POST":
        form = RolesForm(request.POST, instance=rol)
        if form.is_valid():
            rol = form.save(commit=False)
            rol.save()
            return redirect('rol:listaroles')
    else:
        form = RolesForm(instance=rol)
    return render(request, 'actualizar_rol.html', {'form': form})


def eliminar_rol(request, pk):
    print(request, pk)
    rol = get_object_or_404(Roles, pk=pk)
    rol.delete()
    return redirect('rol:listaroles')