from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('filter/<str:priority>/', views.filter_tasks, name='filter_tasks'),
    path('filter/status/<str:status>/', views.filterby_status, name='filterby_status'),
]