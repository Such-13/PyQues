'''import datetime

x = datetime.datetime.now()  # Get current time
print("Current time:", x)

def is_american_date_format(date_str):
    try:
        datetime.datetime.strptime(date_str, '%m-%d-%Y')
        return True
    except ValueError:
        print("Error")
        return False

dob_str = input("Enter date of birth (MM-DD-YYYY): ")

if is_american_date_format(dob_str):
    dob = datetime.datetime.strptime(dob_str, '%m-%d-%Y')
    print("Date of Birth:", dob.date())
else:
    print("Error: Please enter the date of birth in MM-DD-YYYY format.")

y1 = dob  # Make y1 a datetime.datetime object
y2 = datetime.datetime.now()  # Get current time as datetime.datetime object

time_difference = y2 - y1


# Calculate the number of full years
years = time_difference.days // 365  # Exact number of years, ignoring fractional part

if(years>=0):
    print(years)

else:
   print(Error)

  '''

import datetime

def is_american_date_format(date_str):
    try:
        datetime.datetime.strptime(date_str, '%m-%d-%Y')
        return True
    except ValueError:
        return False

dob_str = input("Enter date of birth (MM-DD-YYYY): ")

if is_american_date_format(dob_str):
    dob = datetime.datetime.strptime(dob_str, '%m-%d-%Y').date()
    print("Date of Birth:", dob)
else:
    print("Error: Please enter the date of birth in MM-DD-YYYY format.")
    exit()

today_date = datetime.date.today()
age = today_date.year - dob.year - ((today_date.month, today_date.day) < (dob.month, dob.day))

print("Your current age is:", age)
