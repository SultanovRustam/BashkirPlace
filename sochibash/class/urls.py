from django.urls import path

from . import views

app_name = "class"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.class_create, name="class_create"),
    path("<int:class_id>/edit/", views.class_edit, name="class_edit"),
]
