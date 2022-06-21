from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('views/', views.view, name='view'),
    path('write/', views.write, name='write'),
]