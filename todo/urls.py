from django.urls import path

from todo import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.TaskList.as_view(),name='tasks'),
    # The URL accepts an integer as the id (or primary key, pk) of the task.
    # The TaskDetail will take this pk parameter,
    # select the task from the database by the id,
    # construct a Task object, and pass it to a template.
    path('task/<int:pk>/', views.TaskDetail.as_view(),name='task'),
    path('task/create/', views.TaskCreate.as_view(),name='task-create'),
    path('task/update/<int:pk>/', views.TaskUpdate.as_view(),name='task-update'),
    path('task/delete/<int:pk>/', views.TaskDelete.as_view(),name='task-delete'),


]
