from time import strftime, gmtime

time_object = gmtime()

print(time_object)

print(strftime("%Y/%m/%d %H:%M:%S", time_object))