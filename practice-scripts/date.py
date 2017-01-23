#!/usr/bin/python
import datetime
import pytz
# d = datetime.date(2016, 7, 24) #simple date time
# print(d)
# tday = datetime.date.today() #simple date time
# print(tday)
# print(tday.day)
# print(tday.year)
# print(tday.weekday())# Monday -Sunday (0 -6)
# print(tday.isoweekday())#Monday -Sunday (1 -7)
# tdelta = datetime.timedelta(days=7)
#

# print(tday + tdelta)
# print(tday - tdelta)
# print(tday + tdelta)
#
# bday = datetime.date(2017, 4, 7)
#
# til_bday = bday - tday
# print(til_bday)
# print(til_bday.total_seconds())

# t = datetime.time(9,30,45,10000)
# dt = datetime.datetime(2016,7,4, 12, 30, 30 ,200000)
# # print(t.hour)
# tdelta = datetime.timedelta(hours=12)
# print(dt + tdelta)
#
# print(dt.time())

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
#
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

#----------------------------------->
dt = datetime.datetime(2016, 7 , 27 ,12, 30 , 45,tzinfo=pytz.UTC)
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt)
print(dt_utcnow)

#time zone
# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

for tz in pytz.all_timezones:
    print(tz)
