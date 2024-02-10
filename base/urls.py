from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<str:pk>/', views.update, name='update'),
    path('create/<str:pk>/', views.delete, name='delete'),
]
