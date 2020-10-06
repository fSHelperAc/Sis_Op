from django.urls import path
from . import views


app_name = 'post'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about_me', views.about_me, name='about_me'),
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/',views.post_detail,name='post_detail'),
]