# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date(days):
    """
    Calculate the future date based on the number of days provided.
    
    Parameters:
    days (int): The number of days to add to the current date.
    
    Returns:
    str: The future date in the format "YYYY-MM-DD".
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime(" %Y-%m-%d " )

def main():
    # Part 1: Display the Current Date and Time
    display_current_datetime()

    # Part 2: Calculate a Future Date
    try:
        days = int(input("Enter the number of days to add to the current date:"))
        future_date = calculate_future_date(days)
        print("Future Date:", future_date)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
 