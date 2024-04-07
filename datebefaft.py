from datetime import datetime, timedelta

def find_nth_day_before_after(date_str, n):
    # Convert the input date string to a datetime object
    input_date = datetime.strptime(date_str, "%d/%m/%Y")
    print("Input date is", input_date.strftime("%d/%m/%Y"))

    # Calculate N days before and after the input date
    nth_day_before = input_date - timedelta(days=n)
    nth_day_after = input_date + timedelta(days=n)

    # Get the day of the week for each date
    day_before = nth_day_before.strftime("%d/%m/%Y - %A")
    day_after = nth_day_after.strftime("%d/%m/%Y - %A")

    print(f"{n} days before:", day_before)
    print(f"After {n} days:", day_after)

# Get user input for date and number of days
date_input = input("Enter the date in format DD/MM/YYYY: ")
days_input = int(input("Enter the number of days: "))

find_nth_day_before_after(date_input, days_input)
