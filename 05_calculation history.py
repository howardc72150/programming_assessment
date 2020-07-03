# Component 5

# After each calculation present all previous calculations
# the user has done.

import random
# Code to print the time was found from
# https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import datetime

# Initialize variables

# Manually set the calculation method, shape and dimensions for testing purposes,
# this would've been set by the user previously.
calculation_history = []
calculation_method = "area"
now = datetime.now()

shape = "square"
x = random.randint(1,10)
y = random.randint(1,10)

current_calculation = now.strftime("[%H:%M:%S] {:.0f} x {:.0f} = {:.0f}".format(x,y, x*y))
calculation_history.append(current_calculation)

print("=======================================")
print("Area of a square".format(calculation_method.lower()))
print("{:.0f} x {:.0f}".format(x, y))
print("= {:.0f}".format(x * y))
print("=======================================")
print("Calculation History")
for item in calculation_history:
    print(item)
print("=======================================")