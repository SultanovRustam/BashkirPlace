from django.urls import path

from . import views

app_name = "etnoshop"

urlpatterns = [
    path('', views.shop,
         name='etnoshop'),
]
