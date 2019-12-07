import math

goal_value = 432000
# goal_value size for database table
current_value = float(input("Input starting value\n"))
# current database size after initial formatting
while current_value != goal_value:
    next_value = math.ceil(-current_value / (-current_value + goal_value))
    # finding out x in following equation: current_value - 1/x * current_value = goal_value x is needed to be able to
    # equally delete every xth row to reach the goal_value after some iterations.
    # for example: x is 2 on the first iteration: every 2nd value in table is deleted.
    # x is 4 on second iteration: every 4th value in table is deleted
    # this way after every iteration current_value (dataset value) gets closer to goal_value
    current_value = current_value - (1 / next_value) * current_value
    # calculating dataset value after deletion
    current_value = int(current_value)
    # casting dataset size to int (there is no floating point dataset sizes)
    print("To get to", current_value, "input", next_value)
    # final output after every iteration
