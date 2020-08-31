from model_utils import Choices
from model_utils.models import (
    SoftDeletableModel,
    StatusModel,
    TimeStampedModel,
)

from djangoapps.users.models import User
from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=250)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class TimeSlot(models.Model):
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    num_appointments_per_slot = models.IntegerField(default=5)

    def __str__(self):
        return self.start_timestamp.strftime('%a, %m-%d-%Y, %I:%M %p') + ' - ' + self.end_timestamp.strftime('%I:%M %p')

class Appointment(StatusModel, TimeStampedModel):
    """
    Appointment model.
    """
    STATUS = Choices('pending', 'confirmed', 'canceled', 'done')
    appointment_date = models.DateField()
    test = models.ForeignKey(Test, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT, null=True)
    comments = models.TextField(blank=True, null=True)


