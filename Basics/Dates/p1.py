import datetime
gvr = datetime.date(1956, 1, 31)
print(gvr.year)
print(gvr.month)
print(gvr.day)

d = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)  # Add extra days

print(d+dt)

"""
Day-name Month-name Day-Number, Year
Case sensitive
"""
print(gvr.strftime("%A, %B %d, %Y"))
# This : is mandatory as syntax
message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

now = datetime.datetime.today()
print(now)
print(now.microsecond)

""" Important Question :
What is strptime() ? In python dates?
parsing a string into a datetime object is done
using strptime() function. 
"""
t = "25/1/2023"
print(type(t))
t_datetime = datetime.datetime.strptime(t, "%d/%m/%Y")
print(t_datetime)
print(type(t_datetime))

