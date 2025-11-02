days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday"]
def add_days(start_day, delta):
    idx = (start_day - 1 + delta) % 7
    return days[idx]

print(add_days(5, 2))