from django.urls import path

from . import views

app_name = "meeting"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.profile_create, name="profile_create"),
    path("<int:profile_id>/", views.profile_detail, name="profile_detail"),
    path("profile/<str:username>/", views.profile, name="profile"),
]
