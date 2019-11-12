from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# -----------  para nuestos modelos --------------------
from .models import Cliente

from .forms import ClienteForm

def index(request):
    return render(request, 'app/index.html', {})

def locales(request):
    return render(request, 'app/locales.html', {})

def quienes_somos(request):
    return render(request, 'app/quienes_somos.html', {})

def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/agregarCliente')
    else:
        form = ClienteForm()
        return render(request, 'app/agregar_cliente.html',
                      {'form': form})

def listar_clientes(request):
    # creamos una colección la cual carga TODOS los registos
    clientes = Cliente.objects.all()
    # renderizamos la colección en el template
    return render(request,
        "app/listar_clientes.html", {'clientes': clientes})

def editar_cliente(request, cliente_id):
    # Recuperamos el registro de la base de datos por el id
    instancia= Cliente.objects.get(id=cliente_id)
    # creamos un formulario con los datos del objeto
    form=  ClienteForm(instance=instancia)
    # Compronbamos si se envió el formulario
    if request.method=="POST":
        # Actualizamos el formulario con los datos del objeto
        form= ClienteForm(request.POST, instance=instancia)
        # Si el formulario es valido....
        if form.is_valid():
            #Guardamos el formulario pero sin confirmar aun
            instancia= form.save(commit=False)
            # grabamos!!!
            instancia.save()
    return render(request, "app/editar_cliente.html",{'form':form})            

def borrar_cliente(request, cliente_id):    
    instacia= Cliente.objects.get(id=cliente_id)
    instacia.delete()
    return redirect('/')

# .... Otra forma usando Generics
class Cliente_Create(CreateView):
    model = Cliente
    form_class = ClienteForm
    templates_name = 'app/agregar_cliente.html'
    success_url = reverse_lazy('cliente_crear')

