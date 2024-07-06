from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectCreate.as_view(), name='project-create'),
    path('projects/<str:username>/',
         views.ProjectList.as_view(), name='project-list'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('project/update/<int:pk>/',
         views.ProjectUpdate.as_view(), name='project-update'),
    path('project/delete/<int:pk>/',
         views.ProjectDelete.as_view(), name='project-delete'),
]
