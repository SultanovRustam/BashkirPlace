from news.models import Gallery, News
from rest_framework import serializers


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return self.context['request'].build_absolute_uri(
            obj.image.url)

    class Meta:
        model = Gallery
        fields = ('image',)


class NewsSerializer(serializers.ModelSerializer):
    images = GallerySerializer(many=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = News
        fields = ('title',
                  'pub_date',
                  'text',
                  'author',
                  'iframe_code',
                  'images')
