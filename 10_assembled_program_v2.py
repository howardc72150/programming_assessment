# Assembled program
# Version 2

# Initialize variables
accepted_methods = ["area", "perimeter"]
accepted_shapes = ["square", "triangle", "circle", "rectangle", "parallelogram"]
accepted_units = "kilometers", "kilometer", "km", "meters", "meter", "m", "centimeters", "centimeter", "cm", "millimeters", "millimeter", "mm"
units = "kilometer(s), km, meter(s), m, centimeter(s), cm, millimeter(s) or mm"
current_calculation = []
calculations = []


def print_instructions():
    print("==============================================")
    print("                 Instructions")
    print("==============================================")
    print("Enter the shape you are wanting to use then")
    print("enter whether you're calculating the area or")
    print("the perimeter of the shape. Enter the shapes")
    print("      dimensions. Repeat if desired!")
    print("==============================================")
    print("")


def check_shape(question):
    error = "Please enter either square, triangle, circle, rectangle or parallelogram."
    valid = False
    while not valid:
        response = input(question)
        has_errors = ""
        # Checks if the user input is not an acceptable shape from
        # the `accepted_shapes` variable.
        if response.lower() not in accepted_shapes:
            has_errors = "yes"
        if has_errors != "":
            print(error)
            continue
        else:
            return response.lower()


def check_unit(response):
    error = "Please enter either {}".format(units)
    valid = False
    while not valid:
        response = input(response)
        has_errors = ""
        if response.lower() not in accepted_units:
            has_errors = "yes"
        if has_errors != "":
            print(error)
            continue
        else:
            return response.lower()


def check_method(response):
    error = "Please enter either area or perimeter."
    valid = False
    while not valid:
        response = input(response)
        has_errors = ""
        if response.lower() not in accepted_methods:
            has_errors = "yes"
        if has_errors != "":
            print(error)
            continue
        else:
            return response.lower()


def number_checker(response):
    error = "Please enter a number that is more than zero."
    valid = False
    while not valid:
        try:
            response = float(input(response))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

# Main routine
keep_going = ""
print_instructions()

while keep_going == "":
    current_calculation = []
    print("Available shapes: square, triangle, circle, rectangle or parallelogram.")

    shape = check_shape("Which shape would you like to use? ")
    current_calculation.append(shape)
    unit = check_unit("What is the unit? ")
    method = check_method("Area or perimeter? ")
    current_calculation.append(method)

    if shape == "square":
        if method == "area":
            length = number_checker("Length? ")
            width = number_checker("Width? ")
            neat_calculation = "{:.0f} x {:.0f}".format(length, width)
            answer = length * width
        elif method == "perimeter":
            length = number_checker("Length? ")
            neat_calculation = "4x{:.0f}".format(length)
            answer = length * 4
        current_calculation.append(neat_calculation)
    elif shape == "triangle":
        if method == "area":
            base = number_checker("Base? ")
            height = number_checker("Height? ")
            neat_calculation = "1/2 x {:.0f} x {:.0f}".format(base, height)
            answer = 0.5 * base * height
        if method == "perimeter":
            side_one = number_checker("Side One? ")
            side_two = number_checker("Side Two? ")
            side_three = number_checker("Side Three? ")
            neat_calculation = "{:.0f} + {:.0f} + {:.0f} ".format(side_one, side_two, side_three)
            answer = side_one + side_two + side_three
        current_calculation.append(neat_calculation)


    current_calculation.append(answer)
    calculations.append(current_calculation)

    if 1 >= answer:
        if unit == "kilometers" or "km":
            unit = "kilometer"
        elif unit == "meters" or "m":
            unit = "meter"
        elif unit == "centimeters" or "cm":
            unit = "centimeter"
        elif unit == "millimeters" or "mm":
            unit = "millimeter"
    else:
        if unit == "kilometer" or "km":
            unit = "kilometers"
        elif unit == "meter" or "m":
            unit = "meters"
        elif unit == "centimeter" or "cm":
            unit = "centimeters"
        elif unit == "millimeter" or "mm":
            unit = "millimeters"
    current_calculation.append(unit)

    print("")
    print("=======================================")
    print("Calculating the {} of a {}".format(method, shape.lower()))
    print("=======================================")
    print("")
    print("{}".format(neat_calculation))
    print("= {:.2f} {}".format(answer, unit))
    list = len(calculations)
    if list > 1:
        print("")
        print("Calculation History:")
        for item in calculations:
            print("{} = {:.2f} {}".format(item[2], item[3], item[4]))

    print("")
    keep_going = input("Type <enter> to continue, or anything else to exit.")
    print(calculations)