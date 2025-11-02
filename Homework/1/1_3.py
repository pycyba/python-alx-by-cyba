"""
Task 1.3: Renovation Company

A renovation company has the following price list of services:
• Wall plastering: 100 PLN per square meter of wall
• Painting walls and ceilings: 30 PLN per square meter
• Laying floor panels: 50 PLN per square meter of floor
• Installing baseboards: 40 PLN per linear meter

Write a program that helps estimate the total cost of work based on the dimensions of a rectangular room.
The program should ask for two horizontal dimensions (in meters) and the height, and based on that,
calculate the surface area of the floor, ceiling, and all walls combined, as well as the perimeter of the room (for baseboards).

Then ask the user which types of work should be done.
For example, the question “Should the walls be plastered?” — and the user answers "Y" or "N" for each task.

Finally, depending on the room dimensions and the types of work selected,
the program outputs the total cost to be paid.
"""
price_list = {
    "plastering_walls": 100,       # PLN per m^2 (walls)
    "painting_walls_ceilings": 30, # PLN per m^2 (walls + ceiling)
    "laying_floor_panels": 50,     # PLN per m^2 (floor)
    "baseboards": 40,              # PLN per meter (perimeter)
}

a, b = map(float, input("Give two dimensions of the rectangle (m): ").split())
h = float(input("Give the height of the room (m): "))

walls_area = 2 * (a + b) * h
floor_area = a * b
ceiling_area = floor_area
perimeter = 2 * (a + b)

quantities = {
    "plastering_walls": walls_area,
    "painting_walls_ceilings": walls_area + ceiling_area,
    "laying_floor_panels": floor_area,
    "baseboards": perimeter,
}

labels = {
    "plastering_walls": ("Plaster walls?", "m^2"),
    "painting_walls_ceilings": ("Paint walls and ceiling?", "m^2"),
    "laying_floor_panels": ("Lay floor panels?", "m^2"),
    "baseboards": ("Install baseboards?", "m"),
}

total = 0.0

for key, rate in price_list.items():
    prompt, unit = labels[key]
    ans = input(f"{prompt} (T/N): ").strip().lower()
    if ans.startswith('t'):
        qty = quantities[key]
        subtotal = qty * rate
        print(f"- {key}: {qty:.2f} {unit} × {rate:.2f} PLN = {subtotal:.2f} PLN")
        total += subtotal

print(f"Total: {total:.2f} PLN")

