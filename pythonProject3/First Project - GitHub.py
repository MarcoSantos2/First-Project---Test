
'''
- Crie 1 função a calcula q se aplica tanto para pounds qndo para kg, vc só chama ela com um parametro a
mais para definir o q vc está chamando.
    - Crie 1 função q imprime os textos tanto para kg qnto para pounds
    - Faça 1 pergunta de multipla escolha(1 - Kg to Lbs, 2 - Lbs to Kg) e 1 pergunta para pegar o valor
'''

# Global variables
kg_to_pounds = 1 * 2.205
name_of_unit1 = "pounds"
pounds_to_kg = 1 / 2.205
name_of_unit2 = "Kilograms"
user_input_kgs_or_pds = input("Would you like to convert Kg to Pounds or Pounds to Kg? (Only type 'Kgs' or 'LBS')\n")


# Main function
def units_of_mass_converter(value):
    if user_input_kgs_or_pds.upper() == "KGS":
        return f"{value} Kg(s) is {value * kg_to_pounds} {name_of_unit1}."
    elif user_input_kgs_or_pds.upper() == "LBS":
        return f"{value} pound(s) is {value * pounds_to_kg} {name_of_unit2}."
    else:
        print("I told you to type 'LBS' or 'Kgs', what's wrong with you?")




def validate_and_execute():
    user_input = input("Enter number of unit and I'll convert it.\n")
    try:
        user_input_num = float(user_input)
        if user_input_num > 0:
            calculated_value = units_of_mass_converter(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            print("If you don't know the answer to this one, I don't know what to tell ya")
        elif user_input_num < 0:
            print("Negative mass is only hypothetical, don't get ahead of yourself")
        elif user_input_num == "exit":
            quit()
    except ValueError:
        print("Don't be a smart ass, input a number!")

validate_and_execute()

print("------------------------------------------------------------------------------------")
