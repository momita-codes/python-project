def add_time(start, duration, day=None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Parse start time
    try:
        time, meridian = start.strip().split()
        start_hour, start_minute = map(int, time.split(':'))
    except:
        return "Error: Invalid start time format."

    # Convert start time to 24-hour format
    if meridian.upper() == "PM" and start_hour != 12:
        start_hour += 12
    elif meridian.upper() == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration
    try:
        dur_hour, dur_minute = map(int, duration.strip().split(':'))
    except:
        return "Error: Invalid duration format."

    # Add time
    end_minute = start_minute + dur_minute
    extra_hour = end_minute // 60
    end_minute = end_minute % 60

    end_hour = start_hour + dur_hour + extra_hour
    days_later = end_hour // 24
    end_hour = end_hour % 24

    # Determine new meridian
    if end_hour >= 12:
        meridian = "PM"
    else:
        meridian = "AM"

    display_hour = end_hour % 12
    if display_hour == 0:
        display_hour = 12

    # Final time string
    new_time = f"{display_hour}:{end_minute:02d} {meridian}"

    # Handle day of week
    if day:
        try:
            day_index = days_of_week.index(day.capitalize())
            new_day = days_of_week[(day_index + days_later) % 7]
            new_time += f", {new_day}"
        except:
            return "Error: Invalid day name."

    # Handle (next day) or (n days later)
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


# ---------------- USER INTERACTION ---------------- #

if __name__ == "__main__":
    print("Time Calculator")
    print("----------------------")
    print("Enter time in format: HH:MM AM/PM")
    start = input("Start time (e.g., 11:43 PM): ").strip()
    duration = input("Duration (e.g., 2:20): ").strip()
    day = input("Optional day (e.g., Monday): ").strip()

    if day == "":
        day = None

    result = add_time(start, duration, day)
    print("\n Result:")
    print(result)
