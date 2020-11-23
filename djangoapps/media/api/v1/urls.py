from rest_framework.routers import DefaultRouter

from djangoapps.media.api.v1.views import EditableTextsViewSet, MediaViewSet, NonMediaViewSet

router = DefaultRouter()
router.register(r'editable_texts', EditableTextsViewSet, basename='editable_texts')
router.register(r'media', MediaViewSet, basename='media')
router.register(r'website-pictures', NonMediaViewSet, basename='non-media')

urlpatterns = router.urls
