from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_view, name="main"),
    path('administration/', views.administration,
         name='administration'),
    path("<int:member_id>/", views.member_detail, name="member_detail"),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('elements/', views.ElementsView.as_view(), name='elements'),
]
