# Display Today's Date and Current Time

from datetime import date, datetime 
today = date.today() 
now = datetime.now() 
print("Today's date:", today) 
print("Current date and time:", now) 
print("Date:", now.strftime("%d-%m-%Y")) 
print("Time:", now.strftime("%I:%M:%S %p"))
