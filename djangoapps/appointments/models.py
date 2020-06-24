from model_utils import Choices
from model_utils.models import (
    SoftDeletableModel,
    StatusModel,
    TimeStampedModel,
)

from djangoapps.users.models import User
from django.db import models

class Appointment(SoftDeletableModel, StatusModel, TimeStampedModel):
    """
    Appointment model.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    STATUS = Choices('pending', 'confirmed', 'canceled')
    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
