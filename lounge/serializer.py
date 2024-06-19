from rest_framework import serializers
from lounge.models import *
from common.serializer import MediaURLSerializer


class LoungeImagesSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()

    class Meta:
        model = LoungeImages
        fields = ['id', 'photo']


class LoungeSerializer(serializers.ModelSerializer):
    lounge_images = LoungeImagesSerializer(many=True)

    class Meta:
        model = Lounge
        fields = ['id', 'title', 'price', 'rate_google', 'rate_yandex', 'lounge_images']


class LoungeDetailSerializer(serializers.ModelSerializer):
    lounge_images = LoungeImagesSerializer(many=True)

    class Meta:
        model = Lounge
        fields = ['id', 'title', 'price', 'rate_google', 'rate_yandex', 'phone_number', 'work_time', 'description', 'lounge_images', 'metro']
