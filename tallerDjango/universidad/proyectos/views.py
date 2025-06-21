from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Proyecto
from .form import ProyectoForm, RegistroUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method =='POST':
        form=RegistroUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegistroUserForm()
    
    return render(request, 'registro.html', {'form':form})

def iniciar_sesion(request):
    if request.method == 'POST':
        usuario=request.POST['username']
        clave=request.POST['password']
        user=authenticate(request, username=usuario, password=clave)
        if user:
            login(request, user)
            return redirect('lista_proyectos')
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

#CRUD
@login_required

def lista_proyectos(request):
    proyectos=Proyecto.objects.all()
    return render(request, 'proyectos/lista.html', {'proyectos': proyectos})

@login_required

def agregar_proyectos(request):
    form=ProyectoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_proyectos')
    return render(request, 'proyectos/form.html', {'form':form})

@login_required

def editar_proyectos(request, id):
    proyecto=Proyecto.objects.get(id=id)
    form=ProyectoForm(request.POST or None, instance=proyecto)
    if form.is_valid():
        form.save()
        return redirect('lista_proyectos')
    return render(request,'proyectos/form.html', {'form': form})

@login_required

def eliminar_proyectos(request, id):
    proyecto=Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('lista_proyectos')