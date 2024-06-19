from rest_framework import serializers
from mix.models import *
from common.serializer import MediaURLSerializer


class MixCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MixCategory
        fields = ('id', 'title')
        read_only_fields = fields


class MixSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    tags = serializers.ListSerializer(child=serializers.CharField(source='tag.title'))
    variants = serializers.ListSerializer(child=serializers.CharField(source='variant.title'))

    class Meta:
        model = Mix
        fields = ('id', 'title', 'description', 'tags', 'variants', 'category')
        read_only_fields = fields


class StrengthSerializer(serializers.Serializer):

    class Meta:
        model = Strength
        fields = ('id', 'percentage')
        read_only_fields = fields


class MixDetailSerializer(serializers.ModelSerializer):
    tags = serializers.ListSerializer(child=serializers.CharField(source='tag.title'))
    variants = serializers.ListSerializer(child=serializers.CharField(source='variant.title'))
    strength = StrengthSerializer()

    class Meta:
        model = Mix
        fields = ('id', 'title', 'description', 'tags', 'variants', 'category', 'strength')
        read_only_fields = fields
