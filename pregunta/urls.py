from django.urls import path
from . import views

app_name = 'pregunta'

urlpatterns = [
    path('',  views.get_questionaries, name='home'),
    path('cuestionario/<int:pk>',  views.preguntas_list, name='preguntas_list'),
    path('pregunta/<int:pk>/', views.pregunta_detail, name='pregunta_detail'),
    path('temp',views.populate,name='preg_detail'),
    path('random', views.go_to_random, name='go_to_random'),
    path('pregunta/<int:pk>/next', views.go_to_next, name='go_to_next'),
    path('pregunta/<int:pk>/previous', views.go_to_previous, name='go_to_previous'),
    path('search',views.search,name='search'),
] 