from datetime import date, timedelta 
today = date.today() 
days = 7
new_date = today + timedelta(days=days) 
print("Present date:", today) 
print("Date after adding", days, "days:", new_date) 