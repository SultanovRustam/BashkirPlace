from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NewsViewSet

app_name = 'api'

router = DefaultRouter()

router.register('news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
