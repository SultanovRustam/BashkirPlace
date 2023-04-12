from django.urls import path

from . import views

app_name = "etnoshop"

urlpatterns = [
    path('', views.shop, name='etnoshop'),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
]
