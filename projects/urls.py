from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects.as_view(), name='projects'),
    path('projects/', views.projects.as_view(), name='projects'),
    path('project/<str:pk>', views.project, name='project'),
    path('create-project/', views.createProject.as_view(), name='create-project'),
    path('update-project/<str:pk>/', views.updateProject.as_view(), name='update-project'),
    path('delete-project/<str:pk>/', views.deleteProject.as_view(), name='delete-project'),
]
