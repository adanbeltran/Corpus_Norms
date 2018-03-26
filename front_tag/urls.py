from django.urls import path

from . import views

# definicion de espacio de nombre de aplicacion
app_name = 'front_tag'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>', views.DetailView.as_view() , name = 'detail'),
    # ex: /polls/specifics/12/      ### tomaria estal ultima definion de name="detail"
    #path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]