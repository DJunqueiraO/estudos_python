from time import localtime, strftime

time_object = localtime()

print(time_object)

print(strftime("%Y/%m/%d %H:%M:%S", time_object))