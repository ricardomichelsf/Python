import datetime as dt

data = dt.date(2021, 9, 11)
tday = dt.date.today()
#print(tday, data)

#dt.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = dt.timedelta(hours=12)
print(tday + tdelta)

bday = dt.date(2016, 9, 24)
till_bday = bday - tday
print(till_bday)

dt_agora = dt.datetime.now()
print(dt_agora.strftime('%B %d, %Y\n'))

dt_str = 'July 24, 2016'
dat = dt.datetime.strptime(dt_str, '%B %d, %Y')
print(dat)

# strftime = Dtetime para String
# strptime = String para Datetime