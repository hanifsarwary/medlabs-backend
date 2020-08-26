from django.core.management import BaseCommand
from datetime import datetime, timedelta
from dateutil.rrule import DAILY, MINUTELY, rrule, MO, TU, WE, TH, FR

from djangoapps.appointments.models import TimeSlot

def daterange(start_date, end_date):
  return rrule(DAILY, dtstart=start_date, until=end_date, byweekday=(MO,TU,WE,TH,FR))

def daterange_minute(start_date, end_date):
  return rrule(MINUTELY, dtstart=start_date, until=end_date, byminute=(0, 15, 30, 45))


class Command(BaseCommand):
    help = 'Create a new Partner, or upd'

    def handle(self, *args, **options):
        timeslot_data = []
        current_date = datetime.today().replace(hour=10, minute=0)
        days = daterange(current_date, current_date + timedelta(days=365*4))
        for day in days:
            future_date = day + timedelta(hours=6)
            time_range = daterange_minute(day, future_date)
            ind = 0
            while ind + 1 < len(list(time_range)):
                timeslot_data.append(TimeSlot(
                    start_timestamp=time_range[ind],
                    end_timestamp=time_range[ind + 1],
                    num_appointments_per_slot=4
                ))
                ind +=1

        TimeSlot.objects.bulk_create(timeslot_data)
