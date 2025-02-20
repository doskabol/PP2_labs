#1
import datetime
today = datetime.date.today()
delta = datetime.timedelta(days = 5)

ans = today - delta
print(ans)

#2
import datetime
t = datetime.date.today()
d = datetime.timedelta(days = 1)
y = t - d
tw = t + d

print(y)
print(t)
print(tw)

#3
import datetime 
t = datetime.datetime.now()
r = t.replace(microsecond = 0)
print(r)

#4
import datetime
d1 = datetime.datetime(2006, 9, 19, 12, 0, 0)
d2 = datetime.datetime(2024, 9, 1, 5, 0, 0)
d = (d2 - d1).total_seconds()
print(d)
