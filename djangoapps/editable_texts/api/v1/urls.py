from rest_framework.routers import DefaultRouter

from djangoapps.editable_texts.api.v1.views import EditableTextsViewSet

router = DefaultRouter()
router.register(r'editable_texts', EditableTextsViewSet, basename='editable_texts')

urlpatterns = router.urls
