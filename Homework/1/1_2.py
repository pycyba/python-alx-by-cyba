"""
Task 1.2: Shoe Repair / Days of the Week

The user provides the day of the week (number from 1 to 7) when they drop off shoes at the cobbler,
and the program randomly generates the repair time in days, from 0 to 14 days.

The program should output which day of the week the shoes will be ready for pickup.

Print the pickup day in words, and if you can, also provide information about which week
the pickup will be, e.g., "on Friday this week", "on Thursday next week", or "on Monday in two weeks".
"""
import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

menu = """
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday
7 - Sunday
"""

try:
    x = int(input(f"Pickup day of the week (1-7): \n{menu}"))
    if x < 1 or x > 7:
        print("Error: Pickup day must be between 1 and 7.")
    else:
        time_repair = random.randint(0, 14)
        print(f"Repair time: {time_repair} days")

        pickup_day_idx = (x - 1 + time_repair) % 7
        pickup_day_name = days[pickup_day_idx]

        weeks = time_repair // 7

        if time_repair == 0:
            print(f"Boots are ready immediately on {pickup_day_name}!")
        elif weeks == 0:
            print(f"Boots will be ready on {pickup_day_name} this week.")
        elif weeks == 1:
            print(f"Boots will be ready on {pickup_day_name} next week.")
        else:
            print(f"Boots will be ready on {pickup_day_name} in {weeks} weeks.")

except ValueError:
    print("Error: Please enter a valid number.")