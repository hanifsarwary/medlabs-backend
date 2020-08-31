from rest_framework import serializers

from djangoapps.media.models import EditableText, Media


class EditableTextSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = EditableText
        fields = ('id', 'key', 'value')

class MediaSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Media
        fields = ('id', 'media_image', 'caption')
