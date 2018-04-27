# Create your views here.
from django.shortcuts import render , redirect
from Normas.models import Etiqueta
from .forms import EtiquetaForm


def list_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request , 'etiquetas_list.html' , { 'etiquetas':etiquetas } )

def create_etiqueta(request):
    form = EtiquetaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_etiquetas')
    
    return render (request , 'etiquetas-form.html', {'form': form})

def update_etiqueta(request, id):
    etiqueta = Etiqueta.objects.get(id=id)
    form = EtiquetaForm(request.POST or None, instance=etiqueta)

    if form.is_valid():
        form.save()
        return redirect('list_etiquetas')

    return render(request, 'etiquetas-form.html', {'form': form, 'etiqueta': etiqueta})


def delete_etiqueta(request, id):
    etiqueta = Etiqueta.objects.get(id=id)

    if request.method == 'POST':
        etiqueta.delete()
        return redirect('list_etiquetas')

    return render(request, 'etiq-delete-confirm.html', {'etiqueta': etiqueta})



    