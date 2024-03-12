# importando o submódulo path que tem algumas características
from django.urls import path 

# trazer tudo que está no arquivo views 
from . import views

urlpatterns = [ # criando padrões de URL
    path('', views.index, name='index')
]
