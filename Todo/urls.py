from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask, name='addTask'),
    path('mad/<int:pk>/', views.mad, name='mad'),
    path('mau/<int:pk>/', views.mau, name='mau'),
    path('dele/<int:pk>/', views.dele, name='dele'),
    path('edit/<int:pk>/', views.edit, name='edit'),
]