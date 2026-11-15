import time

print(time.ctime())
time_object = time.localtime()
print(time_object)
Time=time.strftime("%B %d %Y %H:&M:S", time_object)
print(Time)
print(time.asctime(time_object))
print(time.mktime(time_object))