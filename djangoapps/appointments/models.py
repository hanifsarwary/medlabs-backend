from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import (
    SoftDeletableModel,
    StatusModel,
    TimeStampedModel,
)

from djangoapps.users.models import User
from django.db import models


class Category(models.Model):
    PRICE_TYPE = (
        ('CONVENTIONAL', 'CONVENTIONAL'),
        ('RANGE', 'RANGE'))
    parent_category = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=256)
    alias_name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    secondary_description = models.TextField(null=True, blank=True)
    price_type = models.CharField(max_length=16, choices=PRICE_TYPE, default='CONVENTIONAL')
    interval_count = models.PositiveIntegerField(null=True, blank=True)
    start_price = models.PositiveIntegerField(null=True, blank=True)
    interval_price = models.PositiveIntegerField(null=True, blank=True)
    sorting_order = models.IntegerField(default=0)
    icon_image = models.FileField(null=True, blank=True)
    main_image = models.FileField(null=True, blank=True)
    
    class Meta:
        ordering = ['sorting_order', 'id']

    def __str__(self):
        return self.name

class Test(models.Model):
    title = models.CharField(max_length=250)
    available = models.BooleanField(default=True)
    sorting_order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['sorting_order', 'id']

class Panel(models.Model):

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    panel_name = models.CharField(max_length=250)
    tests = models.ManyToManyField(Test)
    price = models.FloatField()
    available = models.BooleanField(default=True)

    sorting_order = models.IntegerField(default=0)

    def __str__(self):
        return self.panel_name

    class Meta:
        ordering = ['sorting_order', 'id']


class TimeSlot(models.Model):
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    appointment_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.start_timestamp.strftime('%a, %m-%d-%Y, %I:%M %p') + ' - ' + self.end_timestamp.strftime('%I:%M %p')


class Appointment(StatusModel, TimeStampedModel):
    """
    Appointment model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS = Choices('pending', 'paid', 'confirmed', 'canceled', 'done')
    status = StatusField()
    appointment_date = models.DateField()
    panels = models.ManyToManyField(Panel)
    total_price = models.FloatField(default=0)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT, null=True)
    comments = models.TextField(blank=True, null=True)
    transaction_details = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-id']

