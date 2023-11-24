def main():
    # Get user input for time
    user_time = input("Enter the time in 24-hour format (e.g., 07:30): ")

    # Convert the user input to hours
    time_in_hours = convert(user_time)

    # Determine the mealtime and output the result
    if 7.0 <= time_in_hours <= 8.0:
        print('breakfast time')
    elif 12.0 <= time_in_hours <= 13.0:
        print('lunch time')
    elif 18.0 <= time_in_hours <= 19.0:
        print('dinner time')


def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time.split(":"))

    # Convert hours and minutes to a float representing the total hours
    total_hours = hours + minutes / 60.0

    return total_hours

if __name__ == "__main__":
    main()
