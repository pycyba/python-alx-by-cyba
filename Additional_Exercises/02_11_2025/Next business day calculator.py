days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday"]

n = int(input("Enter weekday (1-7): "))
if 1 <= n <= 7:
    if n >= 5:  # Fri (5), Sat (6), Sun (7)
        print("Monday")
    else:
        print(days[n])  # next day
else:
    print("Out of range")