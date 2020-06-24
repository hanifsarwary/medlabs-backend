from rest_framework import serializers

from djangoapps.editable_texts.models import EditableText


class EditableTextSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = EditableText
        fields = ('id', 'key', 'value')
