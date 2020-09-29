from django.core.management import BaseCommand
from djangoapps.appointments.jobs import create_bulk_timeslots
class Command(BaseCommand):
    help = 'Create a new Partner, or upd'

    def handle(self, *args, **options):
      create_bulk_timeslots()