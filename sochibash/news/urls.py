from django.urls import path

from . import views

app_name = "news"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.news_create, name="news_create"),
    path("<int:news_id>/", views.news_detail, name="news_detail"),
    path("<int:news_id>/edit/", views.news_edit, name="news_edit"),
    path("profile/<str:username>/", views.profile, name="profile"),
]
