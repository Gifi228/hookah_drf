from rest_framework import serializers
from tobacco.models import *
from common.serializer import MediaURLSerializer


class TobaccoImagesSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()

    class Meta:
        model = TobaccoImages
        exclude = ('tobacco',)
        read_only_fields = ["id", "image"]


class TobaccoListSerializer(serializers.ModelSerializer):
    tobacco_images = TobaccoImagesSerializer(many=True)

    class Meta:
        model = Tobacco
        fields = ['id', 'title', 'taste', 'description', 'tobacco_images']


class TobaccoDetailSerializer(serializers.ModelSerializer):
    tobacco_images = TobaccoImagesSerializer(many=True)
    country = serializers.CharField(source='country.name')
    tag = serializers.ListSerializer(child=serializers.CharField(source='tag.title'))

    class Meta:
        model = Tobacco
        fields = ['id', 'title', 'manufacturer', 'leaf', 'country', 'tobacco_images',
                  'composition', 'strength', 'taste', 'type', 'tag', 'preparation', 'description']