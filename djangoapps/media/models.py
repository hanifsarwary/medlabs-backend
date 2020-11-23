from model_utils.models import TimeStampedModel

from django.db import models
from tinymce.models import HTMLField

class EditableText(TimeStampedModel):
    """
    The "EditableText" model.
    """
    key = models.CharField(max_length=255, db_index=True)
    value = HTMLField(null=True, blank=True)


class Media(TimeStampedModel):
    """
    The "Media" model.
    """
    media_image = models.ImageField(upload_to='media_images')
    caption = models.CharField(max_length=500)

    def __str__(self):
        return self.caption


class NonMedia(models.Model):

    image = models.ImageField(upload_to='website_pictures')
    key = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.key