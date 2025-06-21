from django import forms  
from .models import Proyecto
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

# Formulario para proyectos
class ProyectoForm(forms.ModelForm):  
    class Meta:  
        model = Proyecto  
        fields = '__all__' 

# Formulario para registro de usuarios
class RegistroUserForm(UserCreationForm):  
    class Meta:  
        model = User  
        fields = ['username', 'password1', 'password2']  

