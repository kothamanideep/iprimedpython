import pytz
from datetime import datetime
standard_time=pytz.utc
timezone=pytz.timezone("Africa/Asmera")
print(datetime.now(standard_time))
print(datetime.now(timezone).strftime("%Y-%m-%d  %H:%M:%S"))
timezone=pytz.timezone("America/Araguaina")
print(datetime.now(timezone).strftime("%Y - %m - %d  %H:%M:%S"))

