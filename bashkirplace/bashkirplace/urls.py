from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls')),
    path("about/", include("about.urls", namespace="about")),
    path('admin/', admin.site.urls),

]
