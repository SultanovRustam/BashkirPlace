import base64

from news.models import Gallery, News
from rest_framework import serializers


class GallerySerializer(serializers.ModelSerializer):
    image_base64 = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ('image', 'image_base64')

    def get_image_base64(self, obj):
        with open(obj.image.path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')


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
