from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("main.urls", namespace="main")),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('class/', include('class.urls', namespace='class')),
    path('meeting/', include('meeting.urls', namespace='meetings')),
    path('news/', include('news.urls', namespace='news')),
    path('schedule/', include('schedule.urls', namespace='schedule')),
    path('shop/', include('etnoshop.urls', namespace='etnoshop')),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

handler404 = 'core.views.page_not_found'
