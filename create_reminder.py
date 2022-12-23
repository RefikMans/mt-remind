from datetime import date, timedelta
from ics import Calendar, Event

c = Calendar()
critical = Event()
critical.name = "Musiktage"
date_string = input('Wann finden die Musiktage statt?(YYYY-MM-DD):')
critical_date = date(int(date_string[:4]), int(date_string[5:7]), int(date_string[8:10]))

critical.begin = date_string + str(' 00:00:00')
critical_ending_date = critical_date + timedelta(days = 4)

critical.end = str(critical_ending_date) + str(' 00:00:00')
c.events.add(critical)

reminder_names = ["Instrumentenliste versenden"]
reminder_times = [timedelta(weeks=4)]

for k in range(len(reminder_names)):
    temp = Event()
    temp.name = reminder_names[k]
    temp_date = critical_date - reminder_times[k]
    temp.begin = str(temp_date) + str(' 00:00:00')
    temp.make_all_day()
    
    c.events.add(temp)

with open('reminder.ics', 'w') as cal_file:
    cal_file.writelines(c.serialize_iter())
# and it's done !