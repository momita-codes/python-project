def add_time(start, duration, starting_day=None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Split start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Convert to 24-hour format
    if period == 'PM':
        start_hour += 12 if start_hour != 12 else 0
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    # Split duration
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Add time
    total_minutes = start_minute + dur_minute
    extra_hour = total_minutes // 60
    final_minutes = total_minutes % 60

    total_hours = start_hour + dur_hour + extra_hour
    days_passed = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    final_period = 'AM' if final_hour_24 < 12 else 'PM'
    final_hour_12 = final_hour_24 % 12
    final_hour_12 = 12 if final_hour_12 == 0 else final_hour_12

    # Format time
    new_time = f"{final_hour_12}:{str(final_minutes).zfill(2)} {final_period}"

    # Add weekday
    if starting_day:
        index = days_of_week.index(starting_day.capitalize())
        new_day = days_of_week[(index + days_passed) % 7]
        new_time += f", {new_day}"

    # Add day count info
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
if __name__ == "__main__":
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))
