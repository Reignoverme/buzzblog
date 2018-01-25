from django.urls import path

from . import views

app_name = 'ariticle'
urlpatterns = [
    path('', views.home, name='index'),
    path('post/<str:title>/', views.read, name='read')
]
