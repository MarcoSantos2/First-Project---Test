days_to_minutes = 24 * 60
name_of_unit = "minutes"

print("TESTING FOR GITHUB")


def days_to_unitx(num_of_days, custom_msg):
    return f"{num_of_days} days are {num_of_days*days_to_minutes} {name_of_unit}"

my_var = days_to_unitx(50, 'sup?')

print(my_var)
print("-----------------------------------------------------------------------------------")

kg_to_pounds = 1 * 2.205
kg_to_pounds_number = float(kg_to_pounds)
name_of_unit2 = "pounds"


def units_of_mass_converter(kg_value):
    return f'{kg_value} Kg(s) is {kg_value * kg_to_pounds} {name_of_unit2}'


user_input = input("Enter number of Kg(s) and I'll convert it to pounds\n")
user_input_number = float(user_input)

function_result_Im_looking_for = units_of_mass_converter(user_input_number)
print(function_result_Im_looking_for)

print("-----------------------------------------------------------------------------------")

pounds_to_kg = 1 / 2.205
pounds_to_kg_number = float(pounds_to_kg)
name_of_unit3 = "Kilograms"


def units_of_mass_converter2(pounds_value):
    return f'{pounds_value} pound(s) is {pounds_value * pounds_to_kg} {name_of_unit3}'


user_input2 = input("""Enter number of Pound(s) and I will convert it to Kg(s)\n""")
user_input2_number = float(user_input2)

function_result_Im_looking_for2 = units_of_mass_converter2(user_input2_number)
print(function_result_Im_looking_for2)
print("-----------------------------------------------------------------------------------")











