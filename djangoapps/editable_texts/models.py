from model_utils.models import TimeStampedModel

from django.db import models

class EditableText(TimeStampedModel):
    """
    The "EditableText" model.
    """
    key = models.CharField(max_length=255)
    value = models.TextField()
