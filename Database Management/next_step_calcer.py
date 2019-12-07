import math

goal = 432000
current_value = float(input("Input startvalue\n"))
while current_value != goal:
    next_value = math.ceil(-current_value / (-current_value + goal))
    current_value = current_value - (1 / next_value) * current_value
    current_value = round(current_value, 4)
    print("To get to", current_value, "input", next_value)
