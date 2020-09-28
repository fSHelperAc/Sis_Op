from django.urls import path
from . import views

app_name = 'pregunta'

urlpatterns = [
    path('',  views.preguntas_list, name='home_1'),
    path('<int:pk>/', views.pregunta_detail, name='pregunta_detail'),
    path('temp',views.populate,name='preg_detail'),
    path('random', views.go_to_random, name='go_to_random')

] 