# Global variables
kg_lbs_factor = 2.205
lbs_full_name = "pounds"
kg_full_name = "Kilograms"

# Main function
def mass_converter(value, option):
    str_value = str(value)
    if option == 1:
        text = f"\n{str_value} Kg(s) is {value * kg_lbs_factor} {lbs_full_name}."
    elif option == 2:
        text = f"\n{str_value} pound(s) is {value / kg_lbs_factor} {kg_full_name}."
    return text

def validate_and_execute():
    try:
        user_input_num = float(user_value)
        if user_input_num > 0:
            calculated_value = mass_converter(user_input_num, user_option)
            print(calculated_value)
        elif user_input_num == 0:
            print("If you don't know the answer to this one, I don't know what to tell ya")
        elif user_input_num < 0:
            print("Negative mass is only hypothetical, don't get ahead of yourself")
    except ValueError:
        print("Don't be a smart ass, input a number!")

while 1==1:
    print("-----------------------------------------------------------------------------------\n")
    print("What do you want to convert?\n")
    print("1 - kg to lbs\n")
    print("2 - lbs to kg\n")
    try:
        user_option = int(input("Enter the option number\n"))
        if user_option == 1:
            user_value = input("Enter number of Kg(s) and I'll convert it to pound(s) \n")
            validate_and_execute()
        elif user_option == 2:
            user_value = input("Enter number of Pound(s) and I will convert it to Kg(s) \n")
            validate_and_execute()
        else:
            print("Invalid Option \n")
    except ValueError:
        print("Invalid Option \n")