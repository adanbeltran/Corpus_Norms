# Create your views here.
from django.shortcuts import render , redirect
from .models import Norma
from .forms import NormaForm
from django.http import JsonResponse
from django.core.serializers import serialize
from .componente import TagNorm
from django.core.files import File
import csv, ast , json

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

def etiquetado_automatico(request):
    pretag = request.GET.get('pretag', None)
    text   = request.GET.get('norm',None)
    myList=()
    l = list(myList)
    items=[]
    with open('/Users/ivan/PycharmProjects/front/normas/static/tag/option_tag.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        line = 0 
        for row in reader:
            items.append(row)
            myList = list(items)

    for tag in items:
        if tag[0] == pretag:
            setTags = []
            setTags.append(ast.literal_eval(tag[2]))

    oTagNorm= TagNorm.tag_Norm('', text , setTags)
    for tag in oTagNorm:
        print(tag)

    data = {
        'pretag': str(oTagNorm)
    }
    
    return JsonResponse(data)

    