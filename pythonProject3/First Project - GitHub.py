# Global variables
kg_to_pounds = 1 * 2.205
name_of_unit1 = "pounds"


# Main function
def units_of_mass_converter(kg_value):
    return f"{kg_value} Kg(s) is {kg_value * kg_to_pounds} {name_of_unit1}."


def validate_and_execute():
    try:
        user_input_num = float(user_input)
        if user_input_num > 0:
            calculated_value = units_of_mass_converter(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            print("If you don't know the answer to this one, I don't know what to tell ya")
        elif user_input_num < 0:
            print("Negative mass is only hypothetical, don't get ahead of yourself")
    except ValueError:
        print("Don't be a smart ass, input a number!")

user_input = input("Enter number of Kg(s) and I'll convert it to pounds\n")   #I'm not sure I understand why this is here.
validate_and_execute()

print("-----------------------------------------------------------------------------------")

# Global variables
pounds_to_kg = 1 / 2.205
name_of_unit2 = "Kilograms"


# Main function
def units_of_mass_converter2(pounds_value):
    return f"{pounds_value} pound(s) is {pounds_value * pounds_to_kg} {name_of_unit2}."


def validate_and_execute2():
    try:
        user_input_num2 = float(user_input2)
        if user_input_num2 > 0:
            calculated_value2 = units_of_mass_converter2(user_input_num2)
            print(calculated_value2)
        elif user_input_num2 == 0:
            print("If you don't know the answer to this one, I don't know what to tell ya")
        elif user_input_num2 < 0:
            print("Negative mass is only hypothetical, don't get ahead of yourself")
    except ValueError:
        print("Don't be a smart ass, input a number!")


# Global variable
user_input2 = input("""Enter number of Pound(s) and I will convert it to Kg(s)\n""")
validate_and_execute2()


print("-----------------------------------------------------------------------------------")
