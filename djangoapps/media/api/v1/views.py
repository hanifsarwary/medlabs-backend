from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from djangoapps.media.models import EditableText, Media, NonMedia
from djangoapps.media.api.v1.serializers import EditableTextSerializer, MediaSerializer, NonMediaSerializer


class EditableTextsViewSet(ModelViewSet):
    """
    Viewset for "EditableText".
    """
    queryset = EditableText.objects.all()
    serializer_class = EditableTextSerializer
    permission_classes = [AllowAny]


class MediaViewSet(ModelViewSet):
    """
    Viewset for "EditableText".
    """
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [AllowAny]


class NonMediaViewSet(ModelViewSet):


    serializer_class = NonMediaSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):

        key = self.request.query_params.get('key')
        return NonMedia.objects.filter(key=key)
