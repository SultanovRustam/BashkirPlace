from django.urls import path

from . import views

app_name = "news"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:news_id>/", views.news_detail, name="news_detail"),
    path("profile/<str:username>/", views.profile, name="profile"),
]
