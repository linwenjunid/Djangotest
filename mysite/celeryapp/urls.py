from django.urls import path
from . import views

app_name = 'celeryapp'
urlpatterns = (
    path('run_task', views.run_task, name='run_task'),
)