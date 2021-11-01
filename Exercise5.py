import Number_Entry as e


def check_numbers(number1, number2):

    number1_mod6 = number1 % 6
    number1_mod10 = number1 % 10
    number2_mod6 = number2 % 6
    number2_mod10 = number2 % 10

    result_mod6=False
    result_mod10=False

    if (number1_mod6==0 or number2_mod6==0):
        print("Minimum one number is divisible by 6")
        result_mod6=True
    else:
        print("None of these numbers is divisible by 6")

    if number1_mod10==0 and number2_mod10==0:
            print("Both numbers are divisible by 10")
            result_mod10=True
    else:
            print("Both numbers are not divisible by 10")

    if result_mod6 and result_mod10:
        return True

    return False

number1=e.enter_number("number1")
number2=e.enter_number("number2")
check_numbers(number1, number2)

