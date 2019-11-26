from datetime import datetime,timedelta

# obtain current time
print("=========obtain current time========")
now = datetime.now()
print(now)
print("=========increase or decrease time======")
print(now + timedelta(days=1))
print(now - timedelta(days=1))

# specify specific date and time
print("=========specify specific date and time==========")
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
# decimal places of result means milliseconds
print("======timestamp:decimal places of result means milliseconds=======")
print(dt.timestamp())

# timestamp to datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))
# UTC time
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2015-06-19 18:19:59', '%Y-%m-%d %H:%M:%S')

print(cday)
