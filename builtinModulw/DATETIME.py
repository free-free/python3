#!/usr/bin/env python3
from datetime import datetime
now=datetime.now()
print(now)
print(type(now))
dt=datetime(2015,4,19,12,20)
print(dt)
print(dt.timestamp())
t=1324324221.0
#时间戳转换为本地时间
print(datetime.fromtimestamp(t))
#时间戳转换为UTC时间
print(datetime.utcfromtimestamp(t))

#str to datetime
cday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)
#datetime to str
print(now.strftime('%a,%b %d %H:%M'))
#datetime 加减
from datetime import timedelta
print(now+timedelta(hours=10))
print(now-timedelta(days=1))
print(now+timedelta(days=2,hours=12))
#本地时间转换为UTC时间
from datetime import timezone
tzif=timezone(timedelta(hours=8))
dt=now.replace(tzinfo=tzif)
print(dt)


