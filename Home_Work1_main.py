

def enter_number(name_of_number):
    """
    function asks one number and check the entered value, it gives an error message if it is not an integer
    :param name_of_number: a text to say to the user which kind of number do you ask, eg. age, intervall etc.
    :return: entered number
    """
    while True:
        try:
            number = int(input(f"Please enter a number!  {name_of_number}= "))
            break
        except:
            print("Only numbers, please!")

    return number


#
# name_of_number = a text for asking the number
# between_from, between_to = integer values to define the interval
# only numbers in the given interval are accepted
def number_between(name_of_number, between_from, between_to):
    """
    function asks an integer number in a given interval
    :param name_of_number: a text to say to the user which kind of number do you ask, eg. age, intervall etc.
    :param between_from:
    :param between_to:
    :return:
    """

    while True:
        try:
            entered_number = int(input(f"Please enter a number! {name_of_number}= "))
            if between_from <= entered_number <= between_to:
                return entered_number
                break
            else:
                print(f"That's not a valid option! Only numbers between {between_from} and {between_to}, please!")
        except:
            print("That's not a valid option! Only numbers between  {between_from} and {between_to} , please!")


# *********************************************************+**Ex.1
# function gives out my favourite quote
print("Exercise1 - Famous quote")


def famous_quote(quote):
    """

    :param quote:
    :return:
    """
    print(quote)
    return


my_quote = '"Jede Reise beginnt mit einem ersten Schritt"- Laotse'
famous_quote(my_quote)

print(my_quote.title())
print(my_quote.upper())

# *****************************************************************Ex.2
# all calculations has the result 8
print('\n' "Exercise2 - Number eight")


def number_eight():
    print("5 +3 =", 5 + 3)
    print("11-3 =", 11 - 3)
    print("2 * 4=", 2 * 4)
    print("16/ 2=", int(16 / 2))


number_eight()

# *****************************************************************Ex.3
print('\n' "Exercise3 - Formatting")


# function asks the name and the age and than print it to the console in different formats
def name_age():
    name = input("Enter your name: ")

    while True:
        try:
            age = int(input("Enter your age :"))
            if 0 < age < 201:
                break
            else:
                print("That's not a valid option!Only numbers between 1-200, please!")
        except:
            print("That's not a valid option!Only numbers between 1-200, please!")

    text1 = "Hello, "
    text2 = ". You are "
    text3 = " years old."

    print("Hello, {}. You are {} years old.".format(name.title(), age))
    print(text1 + name + text2 + str(age) + text3)
    print(f"Hello, {name.upper()}. You are {age} years old.")


name_age()

# *****************************************************************Ex.4
print('\n' "Exercise4 - Swap 2 numbers")


def swap_integers():
    x = enter_number("x")
    y = enter_number("y")

    a = x  # a stores the value of x during swap
    x = y
    y = a
    print('\n' "After swap:")
    print("x= ", x)
    print("y= ", y)


swap_integers()

# *****************************************************************Ex.5
print('\n' "Exercise5 - Modulo check")


def check_numbers(my_number1, my_number2):
    number1_mod6 = my_number1 % 6
    number1_mod10 = my_number1 % 10
    number2_mod6 = my_number2 % 6
    number2_mod10 = my_number2 % 10

    result_mod6 = False
    result_mod10 = False

    if number1_mod6 == 0 or number2_mod6 == 0:
        print("Minimum one number is divisible by 6")
        result_mod6 = True
    else:
        print("None of these numbers is divisible by 6")

    if number1_mod10 == 0 and number2_mod10 == 0:
        print("Both numbers are divisible by 10")
        result_mod10 = True
    else:
        print("Both numbers are not divisible by 10")

    if result_mod6 and result_mod10:
        return True

    return False


number1 = enter_number("number1")
number2 = enter_number("number2")
check_numbers(number1, number2)

# *****************************************************************Ex.6
print('\n' "Exercise6 - Summarizer")


def sum_up(sumup_from, sumup_to):
    if sumup_to < sumup_from:
        print("Not valid interval, the second number is smaller than the first! Try it again!")

    else:
        sum = 0
        for x in range(sumup_from, sumup_to + 1):
            sum = sum + x
            print(f"+  {x} ")

        print(f"= {sum}")


number1 = enter_number("sum up from")
number2 = enter_number("sum up to")
sum_up(number1, number2)

# *****************************************************************Ex.7
print('\n' "Exercise7 - Sequencer")


def sequence(snum):
    if snum < 0 or snum > 9:
        print("Number must be between 0 and 9. Please try it again")
    else:
        sequence = ""
        i = 0
        for i in range(0, 10):
            if i != snum:
                sequence = sequence + str(i) + " "

    print(sequence)


takeoff = enter_number("number")

sequence(takeoff)

# *****************************************************************Ex.8
print('\n' "Exercise8  - String check")



def check_string(text):
    # function to check if an "a" to find  on first and last position

    if text.upper().endswith("A") or text.upper()[0] == "A":
        return True


my_text = input("Enter a text for checking: ")  # asking for enter a text

if check_string(my_text):  # check the text and write the result to the console
    print("Your text was checked. There is an 'A' on the first or last place!")
else:
    print("Your text was checked. The first and last character is not an 'A'")


# *****************************************************************Ex.9
print('\n' "Exercise9  -  ASCII Art")


def triangle(rows):
    x = 0
    pattern = ""
    for x in range(0, rows):
        pattern = pattern + "*  "
        print(pattern)


my_rows = number_between(" rows for triangle", 1, 80)

triangle(my_rows)

