import math

goal_value = 432000
# goal_value size for database table
current_value = float(input("Input starting value\n"))
# current database size after initial formatting
while current_value > goal_value:
    index_value = math.ceil(-current_value / (-current_value + goal_value))
    # finding out x in following equation: current_value - 1/x * current_value = goal_value x is needed to be able to
    # equally delete every xth row to reach the goal_value after some iterations.
    # for example: x is 2 on the first iteration: every 2nd value in table is deleted.
    # x is 4 on second iteration: every 4th value in table is deleted
    # this way after every iteration current_value (dataset value) gets closer to goal_value
    current_value = current_value - (1 / index_value) * current_value
    # calculating dataset size after deletion
    current_value = math.ceil(current_value)
    # getting next int (no floating point dataset sizes)
    print("To get to", current_value, "input", index_value)
    # final output after every iteration
