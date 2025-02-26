from django.shortcuts import render, redirect
from .forms import FlightForm


# Create your views here.
def index(request):
    return render(request, 'flights/index.html')

def registrar_vuelo(request):
    return render(request, 'flights/registrar.html')

def listar_vuelos(request):
    return render(request, 'flights/listar.html')

def estadisticas_vuelos(request):
    return render(request, 'flights/estadisticas.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vuelos') 
    else:
        form = FlightForm()

    return render(request, 'flights/registrar.html', {'form': form})
