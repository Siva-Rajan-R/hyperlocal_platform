from enum import Enum
import pytz

class TimeZoneEnum(Enum):
    ...

for tz in pytz.all_timezones:
    TimeZoneEnum._value2member_map_[tz.replace('/','_')]=tz

print(list(TimeZoneEnum._value2member_map_.values()))
