from model_utils import Choices
from model_utils.fields import StatusField
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

class Panel(models.Model):

    panel_name = models.CharField(max_length=250)
    tests = models.ManyToManyField(Test)
    price = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.panel_name


class TimeSlot(models.Model):
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()

    def __str__(self):
        return self.start_timestamp.strftime('%a, %m-%d-%Y, %I:%M %p') + ' - ' + self.end_timestamp.strftime('%I:%M %p')


class Appointment(StatusModel, TimeStampedModel):
    """
    Appointment model.
    """
    STATUS = Choices('pending', 'paid', 'confirmed', 'canceled', 'done')
    status = StatusField()
    appointment_date = models.DateField()
    panels = models.ManyToManyField(Panel)
    total_price = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT, null=True)
    comments = models.TextField(blank=True, null=True)


