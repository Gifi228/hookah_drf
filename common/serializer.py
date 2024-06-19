from rest_framework import serializers


class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, media):
        if not media:
            return None
        try:
            return self.context["request"].build_absolute_uri(media.file.url)
        except Exception:
            return "http://testserver" + str(media.file.url)


class ConfigSerializer(serializers.Serializer):
    text = serializers.CharField()
    created_at = serializers.DateTimeField()
    author = serializers.CharField(source='author.username', max_length=200)
    stars = serializers.FloatField()

