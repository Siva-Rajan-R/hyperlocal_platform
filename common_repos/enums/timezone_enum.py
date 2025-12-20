from enum import Enum
import pytz

class TimeZoneEnum(str, Enum):
    # 🇮🇳 India
    Asia_Kolkata = "Asia/Kolkata"

    # 🇩🇪 Germany
    Europe_Berlin = "Europe/Berlin"

    # 🇺🇸 United States
    America_New_York = "America/New_York"        
    America_Chicago = "America/Chicago"          
    America_Denver = "America/Denver"            
    America_Los_Angeles = "America/Los_Angeles" 



if __name__=="__main__":
    for tz in pytz.all_timezones:
        TimeZoneEnum._value2member_map_[tz.replace('/','_')]=tz

    print(list(TimeZoneEnum._value2member_map_.values()))
