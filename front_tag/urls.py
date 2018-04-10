from django.conf.urls import url 

from .views import ( NormaList )

# definicion de espacio de nombre de aplicacion
app_name = 'front_tag'

urlpatterns = [
    url(r'^norma/', NormaList.as_view(), name='list'),
]