from rest_framework.viewsets import ModelViewSet

from djangoapps.editable_texts.models import EditableText
from djangoapps.editable_texts.api.v1.serializers import EditableTextSerializer


class EditableTextsViewSet(ModelViewSet):
    """
    Viewset for "EditableText".
    """
    queryset = EditableText.objects.all()
    serializer_class = EditableTextSerializer
