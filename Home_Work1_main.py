def enter_number(name_of_number):
    """
    function asks one number and check the entered value, it gives an error message if it is not an integer
    :param name_of_number: a text to say to the user which kind of number do you ask, eg. age, interval etc.
    :return: entered number
    """
    while True:
        try:
            number = int(input(f"Please enter a number!  {name_of_number}= "))
            break
        except ValueError:
            print("Only numbers, please!")

    return number


def number_between(name_of_number, between_from, between_to):
    """
    function asks an integer number in a given interval
    :param name_of_number: a text to say to the user which kind of number do you ask, eg. age, interval etc.
    :param between_from:
    :param between_to:
    :return: selected number-int
    """

    while True:
        try:
            entered_number = int(input(f"Please enter a number! {name_of_number}= "))
            if between_from <= entered_number <= between_to:
                return entered_number
                # break
            else:
                print(f"That's not a valid option! Only numbers between {between_from} and {between_to}, please!")
        except ValueError:
            print("That's not a valid option! Only numbers between  {between_from} and {between_to} , please!")


def exercise1():
    print("Exercise1 - Famous quote")

    # *********************************************************+**Ex.1
    # function gives out my favourite quote
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


def exercise2():
    # *****************************************************************Ex.2
    # all calculations has the result 8
    print('\n' "Exercise2 - Number eight")

    def number_eight():
        print("5 +3 =", 5 + 3)
        print("11-3 =", 11 - 3)
        print("2 * 4=", 2 * 4)
        print("16/ 2=", int(16 / 2))

    number_eight()


def exercise3():
    """
    The method asks your name and age, than formats the entered name and write to the console
    :return:
    """
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
            except ValueError:
                print("That's not a valid option!Only numbers between 1-200, please!")

        text1 = "Hello, "
        text2 = ". You are "
        text3 = " years old."

        print("Hello, {}. You are {} years old.".format(name.title(), age))
        print(text1 + name + text2 + str(age) + text3)
        print(f"Hello, {name.upper()}. You are {age} years old.")

    name_age()


def exercise4():
    """
    The method asks two numbers and then swaps them
    swapped number will be printed to the console
    :return:
    """
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


def exercise5():
    """
    This method asks two numbers and it checks if the given numbers can be divided with 6 or 10
    :return: if one of the numbers can be divided by 6 and one of the number can be divided
     by 10 the function gives back True, otherwise it gives back False
    """
    print('\n' "Exercise5 - Modulo check")

    def check_numbers(my_number1, my_number2):

        result_mod6 = False
        result_mod10 = False

        if my_number1 % 6 == 0 or my_number2 % 6 == 0:
            print("Minimum one number is dividable by 6")
            result_mod6 = True
        else:
            print("None of these numbers is dividable by 6")

        if my_number1 % 10 == 0 and my_number2 % 10==0:
            print("Both numbers are dividable by 10")
            result_mod10 = True
        else:
            print("Both numbers are not dividable by 10")

        if result_mod6 and result_mod10:
           return True

        return False

    number1 = enter_number("number1")
    number2 = enter_number("number2")
    print("Result of modulo check is: ", check_numbers(number1, number2))


def exercise6():
    """
    The method asks an interval of integers and it sums up all numbers between the entered interval
    :return:
    """
    print('\n' "Exercise6 - Summarizer")

    def sum_up(sum_from, sum_to):
        if sum_to < sum_from:
            print("Not valid interval, the second number is smaller than the first! Try it again!")

        else:
            total = 0
            for x in range(sum_from, sum_to + 1):
                total = total + x
                print(f"+  {x} ")

            print(f"= {total}")

    number1 = enter_number("sum up from")
    number2 = enter_number("sum up to")
    sum_up(number1, number2)


def exercise7():
    """
    The method drops out the entered value from the sequence 0-9 and writes the new sequence to the console
    :return:
    """
    print('\n' "Exercise7 - Sequencer")

    def sequence(s_num):
        new_sequence = ""
        if s_num < 0 or s_num > 9:
            print("Number must be between 0 and 9. Please try it again")

        else:
            for i in range(0, 10):
                if i != s_num:
                    new_sequence = new_sequence + str(i) + " "

        print(new_sequence)

    dropout = number_between("I want to drop out the number ", 0, 9)

    sequence(dropout)


def exercise8():
    """
    The method check the entered text if the character "a" or "A" to find in the first or in the last position.
    :return:
    """
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


def exercise9():
    """
    The method write stars in the form of a triangle to the console
    :return:
    """
    print('\n' "Exercise9  -  ASCII Art")

    def triangle(rows):
        for x in range(0, rows):
            print((x + 1) * "*  ")

    my_rows = number_between(" rows for triangle", 1, 80)

    triangle(my_rows)


def start_exercise(text, first_option, last_option):
    """
    Method, to select the exercise, what the user want to try
    :param text: text to say to the user the interval
    :param first_option: from option
    :param last_option: to option
    :return: ---
    """
    while True:
        print("\nPlease choose an Exercise!")
        selection = number_between(text, first_option, last_option)
        if selection > 0:
            # m_name=
            globals()["exercise" + str(selection)]()
        else:
            print("Thank you for running the program!")
            break


start_exercise(" Exercise 1-9 or 0 to exit", 0, 9)
