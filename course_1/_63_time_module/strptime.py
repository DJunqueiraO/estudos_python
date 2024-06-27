from time import strptime, strftime

time_string = '20 April. 2020'
time_object = strptime(time_string, '%d %B. %Y')

print(strftime("%Y/%m/%d", time_object))