from datetime import datetime, date, time, timedelta


a="10:00-12:00"
l=a.split("-")

b=time(int(l[0][:2]), int(l[1][-2:]))
print(b)

