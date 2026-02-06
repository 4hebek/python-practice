# Exercise:
# - weight converter
# - input for weight
# - input for unit (L for pounds, K for kilograms)
# - logic: check the unit entered
# - logic: calculate thwe converter value
# - print the converted value (nice format)
# - Error handling for invalid unit type (need to be k or l - upper/lower, while true)
# - optional stretch: error handle for non numeric weight input. 


import sys

while True:
    try:
        weight = int(input("Enter your weight: "))
        break
    except ValueError:
        print("[ERROR] - Invalid input. Please enter a numeric value for weight.")
        sys.exit()

while True:
    unit = input("Enter the unit (L for pounds, K for kilograms): ").upper()
    if unit == "K":
        converted_weight = weight * 2.2
        print(f"Your weight in pounds is: {converted_weight:.2f} lbs")
        break
    elif unit == "L":
        converted_weight = weight / 2.2
        print(f"Your weight in kilograms is: {converted_weight:.2f} kgs")
        break
    else:
        print("Invalid unit. Please enter 'L' for pounds or 'K' for kilograms!")
