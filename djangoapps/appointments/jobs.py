from datetime import datetime, timedelta
from dateutil.rrule import DAILY, MINUTELY, rrule, MO, TU, WE, TH, FR

from djangoapps.appointments.models import TimeSlot

def daterange(start_date, end_date):
  return rrule(DAILY, dtstart=start_date, until=end_date, byweekday=(MO,TU,WE,TH,FR))

def daterange_minute(start_date, end_date):
  return rrule(MINUTELY, dtstart=start_date, until=end_date, byminute=(0, 30, 60))


def create_bulk_timeslots():
        timeslot_data = []
        current_date = datetime.today().replace(hour=10, minute=0)
        days = daterange(current_date, current_date + timedelta(days=5))
        for day in days:
            future_date = day + timedelta(hours=6)
            time_range = daterange_minute(day, future_date)
            ind = 0
            while ind + 1 < len(list(time_range)):
                print(time_range[ind])
                timeslot_data.append(TimeSlot(
                    start_timestamp=time_range[ind],
                    end_timestamp=time_range[ind + 1]
                ))
                ind +=1
               
        TimeSlot.objects.bulk_create(timeslot_data)
