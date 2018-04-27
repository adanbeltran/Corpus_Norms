from django.urls import path
from .views import list_etiquetas , update_etiqueta , create_etiqueta , delete_etiqueta 


urlpatterns = [
    path('', list_etiquetas , name='list_etiquetas'), 
    path('new', create_etiqueta , name='create_etiqueta' ), 
    path('update/<int:id>', update_etiqueta , name='update_etiqueta') , 
    path('delete/<int:id>', delete_etiqueta , name='delete_etiqueta'),
]