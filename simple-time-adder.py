# Get the current time
import datetime
now = datetime.datetime.now()

# Prompt the user for the number of hours and minutes to add
hours_to_add = int(input("How many hours do you want to add? "))
minutes_to_add = int(input("How many minutes do you want to add? "))

# Add the hours and minutes to the current time
new_time = now + datetime.timedelta(hours=hours_to_add, minutes=minutes_to_add)

# Print the new time
print("The new time is:", new_time.strftime("%Y-%m-%d %H:%M"))