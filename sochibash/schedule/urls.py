from django.urls import path

from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('calendar/', views.schedule_calendar, name='schedule_calendar'),
    path('<int:pk>/', views.schedule_detail, name='schedule_detail'),
]
