
# Getting current date and time using now().

# importing datetime module for now()
import datetime

# for timezone()
import pytz

# using now() to get current time
# current_time = datetime.datetime.now() # plain, anywhere you are
# only in the Philippines ^_^ but in millitary time
# current_time = datetime.datetime.now(pytz.timezone('Asia/Manila'))
current_time = datetime.datetime.now(pytz.timezone('Asia/Manila'))


# Printing value of now.
print(f"Current time at my area is : {current_time}")

# Printing attributes of now().
print("The attributes of now() are :")
# print(f"{current_time.month}/{current_time.day}/{current_time.year}")
print(f"{datetime.date.today()}")
# print(f"{current_time.hour}:{current_time.minute}:{current_time.second}:{current_time.microsecond}")
print(f"{current_time.hour}:{current_time.minute}:{current_time.second}")
