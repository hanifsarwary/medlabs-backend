from rest_framework.routers import DefaultRouter

from djangoapps.media.api.v1.views import EditableTextsViewSet, MediaViewSet

router = DefaultRouter()
router.register(r'editable_texts', EditableTextsViewSet, basename='editable_texts')
router.register(r'media', MediaViewSet, basename='media')

urlpatterns = router.urls
