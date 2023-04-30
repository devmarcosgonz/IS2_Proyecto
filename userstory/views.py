from django.shortcuts import render, get_object_or_404
from .models import UserStory
from .forms import UserStoryForm

# Create your views here.

def lista_userstories(request):
    userstories = UserStory.objects.all().order_by('id_userstory')
    return render(request, 'lista_userstories.html', {'userstories': userstories})

# def usuarios_detail(request, pk):
#     usuario = get_object_or_404(Usuarios, pk=pk)
#     return render(request, 'usuarios/usuarios_detail.html', {'usuario': usuario})


def crear_userstory(request):
    if request.method == "POST":
        form = UserStoryForm(request.POST)
        if form.is_valid():
            userstory = form.save(commit=False)
            userstory.save()
            userstories = UserStory.objects.all().order_by('id_userstory')
            return render(request, 'lista_userstories.html', {'userstories': userstories})
    else:
        form = UserStoryForm()
    return render(request, 'crear_userstory.html', {'form': form})


def actualizar_userstory(request, pk):
    userstory = get_object_or_404(UserStory, pk=pk)
    if request.method == "POST":
        form = UserStoryForm(request.POST, instance=userstory)
        if form.is_valid():
            userstory = form.save(commit=False)
            userstory.save()
            userstories = UserStory.objects.all().order_by('id_userstory')
            return render(request, 'lista_userstories.html', {'userstories': userstories})
    else:
        form = UserStoryForm(instance=userstory)
    return render(request, 'actualizar_userstory.html', {'form': form})


def eliminar_userstory(request, pk):
    print(request, pk)
    userstory = get_object_or_404(UserStory, pk=pk)
    userstory.delete()
    userstories = UserStory.objects.all().order_by('id_userstory')
    return render(request, 'lista_userstories.html', {'userstories': userstories})
