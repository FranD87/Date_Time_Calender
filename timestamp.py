# A Timestamp is encoded information generally used in UNIX, which indicates the date and time at which a particular event has occured


# Datetime to Timestamp
# from datetime import datetime
#
# dt = datetime.now()
#
# ts = datetime.timestamp(dt)
#
# print('Date and time is:', dt)
#
# print('Timestamp is:', ts)


# Get Timestamp usinf Time module
# import time
#
# x = time.time()
#
# print("Timestamp", x)

# Get Timestamp using calender module
# import calendar
# import time
#
# current_GMT = time.gmtime()
#
# ts = calendar.timegm(current_GMT)
#
# print("Current timestamp:", ts)


# Convert Timestamp to Datetime (format)

# from datetime import datetime
#
# ts = 1617295943.17321
#
# dt = datetime.fromtimestamp(ts)
#
# print("The date and time is:", dt)

# Convert Timestamp to String

# from datetime import datetime
#
# ts = 1625309472.357246
#
# date_time = datetime.fromtimestamp(ts)
#
# str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
#
# print("Result 1:", str_date_time)
#
# str_date = date_time.strftime("%d %B, %Y")
#
# print("Result 2:", str_date)
#
# str_time = date_time.strftime("%I%p %M:%S")
#
# print("Result 3:", str_time)







