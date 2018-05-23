# Create your views here.
from django.shortcuts import render , redirect
from django.apps import apps
from .forms import EtiquetaForm
from django.http import JsonResponse
from django.http import HttpResponse
import json
import requests


def list_etiquetas(request):
    etiquetas = apps.get_model('normas','Etiqueta').objects.all()
    return render(request , 'etiquetas_list.html' , { 'etiquetas':etiquetas } )

def create_etiqueta(request):
    form = EtiquetaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_etiquetas')
    
    return render (request , 'etiquetas-form.html', {'form': form})

def update_etiqueta(request, id):
    etiqueta = apps.get_model('normas','Etiqueta').objects.get(id=id)
    form = EtiquetaForm(request.POST or None, instance=etiqueta)

    if form.is_valid():
        form.save()
        return redirect('list_etiquetas')

    return render(request, 'etiquetas-form.html', {'form': form, 'etiqueta': etiqueta})


def delete_etiqueta(request, id):
    etiqueta = apps.get_model('normas','Etiqueta').objects.get(id=id)

    if request.method == 'POST':
        etiqueta.delete()
        return redirect('list_etiquetas')

    return render(request, 'etiq-delete-confirm.html', {'etiqueta': etiqueta})

def data_etiqueta(request):
    ids = request.GET.__getitem__('ids')
    etiqueta = apps.get_model('normas','Etiqueta').objects.get(id=ids)
    #print(etiqueta.etiqueta_text)
    #data = str('[{"id":"1", "parent" : "#","text":"SVO"},{ "id" : "2", "parent" : "1", "text" : "SUJETO" }]')
    # data = str('["SVO",{"text" : "SVO","state" : {"opened" : true,"selected" : true},"children" : [{ "text" : "SUJETO" },"VERBO", "PREDICADO"]}]')
    #data = str('[{ "id" : "ajson1", "parent" : "#", "text" : "Simple root node" },{ "id" : "ajson3", "parent" : "ajson1", "text" : "Child 1" }]')
    data = str(recursiva(eval(etiqueta.etiqueta_text)))
    print(data) 
    return  JsonResponse( json.loads("["+data+"]") , safe=False)


def recursiva(box):
    boxes = not isinstance(box, (list, tuple)) and [box] or box
    padres = []
    hijos = []
    indice = None
    id_padre = None
    def pegar(arry , idx , id_padre ): 
        #print (arry ,  idx , id_padre , indice)
        arry2 = not isinstance(arry, (list, tuple)) and [arry] or arry
        for item in arry2:
            if ( isinstance ( item, str ) ):
                if id_padre is None:
                    #padres.append( [item , idx , None ] )
                    padres.append('{"id" : "'+str(idx)+'" , "parent" : "#" , "text" : "'+(str(item)).replace('\'','"') +'"} ')
                    idx += 1 
                else:
                    #padres.append( [item , idx , id_padre ] )
                    padres.append('{"id" : "'+str(idx)+'" , "parent" : "'+str(id_padre)+'", "text" : "'+(str(item)).replace('\'','"') +'"} ')
                    idx += 1
            elif ( isinstance( item, list) ):
                #padres.append( [item , idx , id_padre ] )
                padres.append('{"id" : "'+str(idx)+'" , "parent" : "'+str(id_padre)+'", "text" : "'+(str(item)).replace('\'','"') +'"} ')
                idx+=1
        return idx
    for box in boxes:
        #print( prof , str(i) , box , "*"
        value = []
        if ( isinstance ( box, str ) ):
            indice = pegar ( box , 0 , None )
            id_padre = 0
        elif ( isinstance( box, list) ):
            indice = pegar(box, indice , id_padre )    
            id_padre = indice    
    s = ','.join(padres)
    return(s)


