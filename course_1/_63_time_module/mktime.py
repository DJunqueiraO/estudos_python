from time import mktime, ctime

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = mktime(time_tuple)

print(time_string)
print(ctime(time_string))