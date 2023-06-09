from django.shortcuts import render, get_object_or_404
from .models import UserStory
from .forms import UserStoryForm
from sprint.models import Sprints
# Para el Burndown Chart
from django.views import View
from django.db.models import Sum
import plotly #used for plotting
import pandas as pd #used to handle dataframes
import plotly.express as px
import plotly.offline as opy
from datetime import datetime, timedelta


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


#User Stories sin Sprint

def lista_sinsprint(request):
    userstories = UserStory.objects.filter(id_sprint__isnull=True)
    return render(request, 'lista_sinsprint.html', {'userstories': userstories})


#Tablero Kanban

def kanban_board(request):
    to_do = UserStory.objects.filter(id_estado=1)
    doing = UserStory.objects.filter(id_estado=2)
    done = UserStory.objects.filter(id_estado=3)
    return render(request, 'tablero_kanban.html', {'to_do': to_do, 'doing': doing, 'done': done})


#Burndown Chart

def burndown_list(request):
    sprints = Sprints.objects.all().order_by('id_sprint')
    return render(request, 't_burndown_list.html', {'sprints': sprints})


def burndown_chart(request, pk):
    print(request, pk)
    # extraccion de fechas
    sprint_f_inicio = Sprints.objects.filter(id_sprint=pk).values_list('fecha_inicio', flat=True).first()
    year1 = sprint_f_inicio.year
    month1 = sprint_f_inicio.month
    day1 = sprint_f_inicio.day

    sprint_f_fin = Sprints.objects.filter(id_sprint=pk).values_list('fecha_fin', flat=True).first()
    year2 = sprint_f_fin.year
    month2 = sprint_f_fin.month
    day2 = sprint_f_fin.day

    # Variables de las fechas (extremos del eje x)
    fecha_inicio = datetime(year1, month1, day1)
    fecha_fin = datetime(year2, month2, day2)

    # Calcular puntos intermedios de la fecha de inicio y fin del Sprint
    cantidad_puntos_intermedios = 8
    puntos_intermedios = calcular_puntos_intermedios_fechas(fecha_inicio, fecha_fin, cantidad_puntos_intermedios)

    # Asignar los puntos intermedios hallados a variables distintas
    fecha_intermedia1 = puntos_intermedios[0].strftime('%Y-%m-%d')
    fecha_intermedia2 = puntos_intermedios[1].strftime('%Y-%m-%d')
    fecha_intermedia3 = puntos_intermedios[2].strftime('%Y-%m-%d')
    fecha_intermedia4 = puntos_intermedios[3].strftime('%Y-%m-%d')
    fecha_intermedia5 = puntos_intermedios[4].strftime('%Y-%m-%d')
    fecha_intermedia6 = puntos_intermedios[5].strftime('%Y-%m-%d')
    fecha_intermedia7 = puntos_intermedios[6].strftime('%Y-%m-%d')
    fecha_intermedia8 = puntos_intermedios[7].strftime('%Y-%m-%d')

    # Hallar la totalidad de los Story Point del Sprint
    us = UserStory.objects.filter(id_sprint=pk)
    total_history_points = us.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0

    # filtrando los US por fecha para poder sumar sus story points (f=fecha)
    f1 = UserStory.objects.filter(id_sprint=pk, fecha_fin__lte=fecha_inicio.strftime('%Y-%m-%d'))
    f2 = UserStory.objects.filter(id_sprint=pk, fecha_fin__lte=fecha_intermedia1)
    f3 = UserStory.objects.filter(id_sprint=pk, fecha_fin__lte=fecha_intermedia2)
    f4 = UserStory.objects.filter(id_sprint=pk, fecha_fin__lte=fecha_intermedia3)
    f5 = UserStory.objects.filter(id_sprint=pk, fecha_fin__lte=fecha_intermedia4)
    f6 = UserStory.objects.filter(id_sprint=pk, fecha_fin__lte=fecha_intermedia5)
    f7 = UserStory.objects.filter(id_sprint=pk, fecha_fin__lte=fecha_intermedia6)
    f8 = UserStory.objects.filter(id_sprint=pk, fecha_fin__lte=fecha_intermedia7)
    f9 = UserStory.objects.filter(id_sprint=pk, fecha_fin__lte=fecha_intermedia8)
    f10 = UserStory.objects.filter(id_sprint=pk, fecha_fin__lte=fecha_fin.strftime('%Y-%m-%d'))

    # auxiliar para calcular el story point completados de los US hasta cierta fecha (a=auxiliar, que suma)
    a1 = f1.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0
    a2 = f2.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0
    a3 = f3.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0
    a4 = f4.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0
    a5 = f5.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0
    a6 = f6.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0
    a7 = f7.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0
    a8 = f8.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0
    a9 = f9.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0
    a10 = f10.aggregate(total_points=Sum('story_point')).get('total_points', 0) or 0

    # hallando la "y" del punto p=(x, y). Restando del total, la cantidad de tarea realizada (total - auxiliar)
    py1 = total_history_points - a1
    py2 = total_history_points - a2
    py3 = total_history_points - a3
    py4 = total_history_points - a4
    py5 = total_history_points - a5
    py6 = total_history_points - a6
    py7 = total_history_points - a7
    py8 = total_history_points - a8
    py9 = total_history_points - a9
    py10 = total_history_points - a10

    # hallando los números para formar la trayectoria ideal, que acompañara a los puntos hallados arriba
    numbers = generate_numbers_between(total_history_points, 0)
    numero_intermedio1 = numbers[0]
    numero_intermedio2 = numbers[1]
    numero_intermedio3 = numbers[2]
    numero_intermedio4 = numbers[3]
    numero_intermedio5 = numbers[4]
    numero_intermedio6 = numbers[5]
    numero_intermedio7 = numbers[6]
    numero_intermedio8 = numbers[7]

    # Datos para el gráfico
    dates = [fecha_inicio.strftime('%Y-%m-%d'), fecha_intermedia1, fecha_intermedia2, fecha_intermedia3, fecha_intermedia4, 
             fecha_intermedia5, fecha_intermedia6, fecha_intermedia7, fecha_intermedia8, fecha_fin.strftime('%Y-%m-%d')]
    heights = [py1, py2, py3, py4, py5, py6, py7, py8, py9, py10]
    ideales = [total_history_points, numero_intermedio1, numero_intermedio2, numero_intermedio3, numero_intermedio4,
                numero_intermedio5, numero_intermedio6, numero_intermedio7, numero_intermedio8, 0]

    # Crear DataFrame con los datos
    data = {'Date': dates, 'Story Point': heights, 'Ideal': ideales}

    #Create the pandas DataFrame
    df = pd.DataFrame(data)

    # Convertir la columna 'date' al tipo de dato 'datetime'
    df['Date'] = pd.to_datetime(df['Date'])

    # Crear el gráfico de línea utilizando Plotly Express
    fig = px.line(df, x='Date', y= ['Story Point', 'Ideal'], markers=True, width=1000, height=600)

    # Configuraciones adicionales para el gráfico
    fig.update_traces(textposition="top center", marker_size=10)
    fig.update_layout(title_text='Burndown Chart', title_x=0.5, title_font=dict(size=24))

    chart = opy.plot(fig, auto_open=False, output_type='div')

    return render(request, 't_burndown_chart.html', {'chart': chart})


# Función para calcular los puntos intermedios entre dos fechas
def calcular_puntos_intermedios_fechas(fecha_inicio, fecha_fin, cantidad_puntos):
    delta = (fecha_fin - fecha_inicio) / (cantidad_puntos + 1)
    puntos_intermedios = []
    for i in range(1, cantidad_puntos + 1):
        punto_intermedio = fecha_inicio + delta * i
        puntos_intermedios.append(punto_intermedio)
    return puntos_intermedios


# Función para calcular los números intermedios entre dos números para la trayectoria ideal del gráfico
def generate_numbers_between(start, end):
    # Calcula la diferencia entre los números
    difference = end - start

    # Calcula el espacio entre cada número generado
    interval = difference / 9

    # Genera los 8 números entre los extremos
    numbers = [start + (i * interval) for i in range(1, 9)]

    return numbers