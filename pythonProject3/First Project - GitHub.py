"""
days_to_minutes = 24 * 60
name_of_unit = "minutes"

def days_to_unitx(num_of_days, custom_msg):
    return f"{num_of_days} days are {num_of_days*days_to_minutes} {name_of_unit}"

my_var = days_to_unitx(50, 'sup?')

print(my_var)
"""

# My global variables
kg_to_pounds = 1 * 2.205
kg_to_pounds_number = float(kg_to_pounds)
name_of_unit2 = "pounds"


# My main function
def units_of_mass_converter(kg_value):
    if kg_value > 0:
        return f'{kg_value} Kg(s) is {kg_value * kg_to_pounds} {name_of_unit2}'
    elif kg_value == 0:
        return "If you don't know the answer to this one, I don't know what to tell ya"
    else:
        return "Negative mass is only hypothetical, don't get ahead of yourself"


# Global Variable
user_input = input("Enter number of Kg(s) and I'll convert it to pounds\n")


# HERE I AM TRYING TO CREATE AN IF ELSE STATEMENT FUNCTION SO THE USER CAN ONLY INPUT DIGITS AND NOT STRINGS
def input_only_dig():
    if user_input.isdigit():
        user_input_number = float(user_input)
        function_result_Im_looking_for = units_of_mass_converter(user_input_number)
        print(function_result_Im_looking_for)
    else:
        print("Don't be a smart ass, input a number!")


# This is called "calling" a function. I'm not sure why it works without syntax like "print".
# It is calling the function above. Without doing this, the program crashes when the user inputs text.
input_only_dig()

print("-----------------------------------------------------------------------------------")

pounds_to_kg = 1 / 2.205
pounds_to_kg_number = float(pounds_to_kg)
name_of_unit3 = "Kilograms"


def units_of_mass_converter2(pounds_value):
    if pounds_value >= 0:
        return f'{pounds_value} pound(s) is {pounds_value * pounds_to_kg} {name_of_unit3}'
    elif pounds_value == 0:
        return "If you don't know the answer to this one, I don't know what to tell ya"
    else:
        return "Negative mass is only hypothetical, don't get ahead of yourself"

units_of_mass_converter2(pounds_value)
user_input2 = input("""Enter number of Pound(s) and I will convert it to Kg(s)\n""")

def input_only_dig2():
    if user_input.isdigit():
        user_input2_number = float(user_input2)
        function_result_Im_looking_for2 = units_of_mass_converter2(user_input2_number)
        print(function_result_Im_looking_for2)
    else:
        print("Don't be a smart ass, input a number!")


input_only_dig()

print("-----------------------------------------------------------------------------------")








