




from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.graph_view, name='graph'),
    path('calculation/', views.calculate, name='calculate'),
    
]
