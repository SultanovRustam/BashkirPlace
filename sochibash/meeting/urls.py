from django.urls import path

from . import views

app_name = "meeting"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.profile_create, name="profile_create"),
    path("delete/", views.profile_delete, name="profile_delete"),
    path("<int:profile_id>/", views.profile_detail, name="profile_detail"),
    path("<int:profile_id>/edit/", views.profile_edit, name="profile_edit"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("<int:profile_id>/add_comment/",
         views.add_comment, name="add_comment")
]
