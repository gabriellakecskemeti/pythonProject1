def enter_number(name_of_number):
    while True:
        try:
            number = int(input(f"Please enter a number!  {name_of_number}= "))
            break
        except ValueError:
            print("Only numbers, please!")
    return number


def interval_entry(name_of_number, interval_from, interval_to):
    while True:
        try:
            entered_number = int(input(f"Please enter a number! {name_of_number}= "))
            if interval_from <= entered_number <= interval_to:
                return entered_number
                break
            else:
                print(f"That's not a valid option!Only numbers between {interval_from} and {interval_to}, please!")
        except ValueError:
            print("That's not a valid option!Only numbers between  {interval_from} and {interval_to} , please!")
