from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('skill/<int:pk>/', views.skill_detail, name='skill_detail'),
    path('skill/new/', views.skill_create, name='skill_create'),
    path('skill/<int:pk>/edit/', views.skill_update, name='skill_update'),
    path('skill/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
]
