from django.urls import path 
from django.conf.urls import url
from .views import list_normas , update_norma , create_norma , delete_norma , etiquetado_automatico


urlpatterns = [
    #url(r'^norma/', NormaList.as_view(), name='list'),
    #url(r'^$', NormaList.as_view(), name='list'),
    #url(r'^(?P<pk>\d+)$', NormaDetail.as_view(), name='detail'),
    #url(r'^nuevo$', NormaCreation.as_view(), name='new'),
    #url(r'^editar/(?P<pk>\d+)$', NormaUpdate.as_view(), name='edit'),
    path('' , list_normas , name='list_normas'), 
    path('new' , create_norma , name='create_norma' ), 
    path('update/<int:id>' , update_norma , name='update_norma') , 
    path('delete/<int:id>' , delete_norma , name='delete_norma'),
    path('update/normas/ajax/etiquetado_automatico/', etiquetado_automatico, name='etiquetado_automatico'),
]