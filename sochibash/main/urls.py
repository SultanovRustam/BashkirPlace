from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.MainView.as_view(), name="main"),
    path('administration/', views.administration,
         name='administration'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('elements/', views.ElementsView.as_view(), name='elements'),
    path('generic/', views.GenericView.as_view(), name='generic'),
]
