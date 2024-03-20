# importando o submódulo path que tem algumas características
from django.urls import path 

# trazer tudo que está no arquivo views 
from . import views

app_name = 'polls'

urlpatterns = [ # criando padrões de URL
    path('', views.index, name='index'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote')
]
