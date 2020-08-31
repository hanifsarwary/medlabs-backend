from model_utils.models import TimeStampedModel

from django.db import models

class EditableText(TimeStampedModel):
    """
    The "EditableText" model.
    """
    key = models.CharField(max_length=255)
    value = models.TextField()


class Media(TimeStampedModel):
    """
    The "Media" model.
    """
    media_image = models.ImageField(upload_to='media_images')
    caption = models.CharField(max_length=500)

    def __str__(self):
        return self.caption
