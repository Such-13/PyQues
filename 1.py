import datetime

# Function to check if a date string is in American date format (MM-DD-YYYY)
def is_american_date_format(date_str):
    try:
        datetime.datetime.strptime(date_str, '%m-%d-%Y')  # Attempt to parse the date string
        return True  # Return True if parsing succeeds
    except ValueError:
        return False  # Return False if parsing fails

# Prompt the user to enter their date of birth in MM-DD-YYYY format
dob_str = input("Enter date of birth (MM-DD-YYYY): ")

# Check if the entered date of birth is in American date format
if is_american_date_format(dob_str):
    dob = datetime.datetime.strptime(dob_str, '%m-%d-%Y').date()  # Convert the date string to a date object
    print("Date of Birth:", dob)  # Print the date of birth
else:
    print("Error: Please enter the date of birth in MM-DD-YYYY format.")  # Error message if date format is incorrect
    exit()  # Exit the program if the date format is incorrect

# Get today's date
today_date = datetime.date.today()

# Calculate the age based on the date of birth and today's date
age = today_date.year - dob.year - ((today_date.month, today_date.day) < (dob.month, dob.day))

# Print the calculated age
print("Your current age is:", age)
