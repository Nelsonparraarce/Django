from django.shortcuts import render
from . forms import InputForm
# Create your views here.

def forms(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['texto']
            
            # Llamar a la función para contar las palabras
            num_palabras, num_caracteres, num_mayusculas = contar_palabras(texto)
            return render(request, 'resultado.html', {
                'num_palabras': num_palabras,
                'num_caracteres': num_caracteres,
                'num_mayusculas': num_mayusculas
            })
    else:
        form = InputForm()
    
    return render(request, 'index.html', {'form': form})

def contar_palabras(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres = len(texto.replace(" ", ""))
    num_mayusculas = sum(1 for letra in texto if letra.isupper())
    
    return num_palabras, num_caracteres, num_mayusculas
