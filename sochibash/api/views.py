from news.models import News
from rest_framework import viewsets

from .serializers import NewsSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    search_fields = '^text'
