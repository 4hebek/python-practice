# Exercise:
# - weight converter
# - input for weight
# - input for unit (L for pounds, K for kilograms)
# - logic: check the unit entered
# - logic: calculate thwe converter value
# - print the converted value (nice format)
# - Error handling for invalid unit type (need to be k or l - upper/lower, while true)
# - optional stretch: error handle for non numeric weight input. 


try:
    input_weight = float(input("Enter your weight: "))
    input_unit = input("Enter the unit (kg/lb): ").strip().lower() # 
    
    if input_unit == "kg":
        weight_in_lb = input_weight * 2.20462
        print(f"Your weight in pounds is: {weight_in_lb:.2f} lb")
    elif input_unit == "lb":
        weight_in_kg = input_weight / 2.20462
        print(f"Your weight in kilograms is: {weight_in_kg:.2f} kg")
    else:
        print("Invalid unit. Please enter 'kg' for kilograms or 'lb' for pounds.")
except ValueError:
    print("Input your weight in numeric format.")
