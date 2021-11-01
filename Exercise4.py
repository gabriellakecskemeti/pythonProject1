import Number_Entry as e


def swap_integers():
    x = e.enter_number("x")
    y = e.enter_number("y")

    a = x  # a stores the value of x during swap
    x = y
    y = a
    print('\n' "After swap:")
    print("x= ", x)
    print("y= ", y)


swap_integers()
