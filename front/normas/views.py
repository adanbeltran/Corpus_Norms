# Create your views here.
from django.shortcuts import render , redirect
from .models import Norma
from .forms import NormaForm


def list_normas(request):
    normas = Norma.objects.all()
    return render(request , 'normas_list.html' , { 'normas':normas } )

def create_norma(request):
    form = NormaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_normas')
    
    return render (request , 'normas-form.html', {'form': form})

def update_norma(request, id):
    norma = Norma.objects.get(id=id)
    form = NormaForm(request.POST or None, instance=norma)

    if form.is_valid():
        form.save()
        return redirect('list_normas')

    return render(request, 'normas-form.html', {'form': form, 'norma': norma})


def delete_norma(request, id):
    norma = Norma.objects.get(id=id)

    if request.method == 'POST':
        norma.delete()
        return redirect('list_normas')

    return render(request, 'norm-delete-confirm.html', {'norma': norma})



    