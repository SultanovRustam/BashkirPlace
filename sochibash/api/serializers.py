from news.models import Gallery, News
from rest_framework import serializers


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(
                f"https://xn--80abwaizni9ce0b.xn--p1ai{obj.image.url}")
        return obj.image.url

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
