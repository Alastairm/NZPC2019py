import datetime
import sys

stdin_lines = []
for _line in sys.stdin:
    stripped = _line.strip()
    if not stripped: break
    stdin_lines.append(stripped)


departure_city = stdin_lines[0]
departure_time_local = stdin_lines[1]
departure_tz = stdin_lines[2]

arrival_city = stdin_lines[3]
arrival_tz = stdin_lines[4]

flight_time = stdin_lines[5]


def datetime_from_str(dts):
    month, day, time = dts.strip().split()
    hour, minute = time.split(':')
    return datetime.datetime(1, int(month), int(day), int(hour), int(minute))

departure_time = datetime_from_str(departure_time_local)


def dtd_from_tz_str(tzs):
    tzs = tzs.strip()
    sign = tzs[0]
    hours, minutes = tzs[1:].split(':')
    hours = int(hours)
    minutes = int(minutes)
    if sign == '+':
        difference = datetime.timedelta(hours=hours, minutes=minutes)
    elif sign == '-':
        difference = datetime.timedelta(hours=-hours, minutes=-minutes)
    return difference

departure_delta = dtd_from_tz_str(departure_tz)
arrival_delta = dtd_from_tz_str(arrival_tz)
tz_delta = arrival_delta - departure_delta


def dtd_from_time_str(timestr):
    hour, minute = timestr.split(':')
    hour = int(hour)
    minute = int(minute)
    return datetime.timedelta(hours=hour, minutes=minute)

flight_delta = dtd_from_time_str(flight_time)


total_delta = tz_delta + flight_delta

arrival_time = departure_time + total_delta

def calculate_day(departure_td, arrival_td):
    if departure_td.day == arrival_td.day:
        return "same day"
    else:
        return "following day"

a_day = calculate_day(departure_time, arrival_time)

d_month = str(departure_time.month).zfill(2)
d_day = str(departure_time.day).zfill(2)
d_hour = str(departure_time.hour).zfill(2)
d_minute = str(departure_time.minute).zfill(2)
departure = f"Departs {departure_city} {d_month} {d_day} {d_hour}:{d_minute}"

a_hour = str(arrival_time.hour).zfill(2)
a_minute = str(arrival_time.minute).zfill(2)
arrival = f"Arrives {arrival_city} {a_hour}:{a_minute} {a_day}"

print(departure)
print(arrival)
