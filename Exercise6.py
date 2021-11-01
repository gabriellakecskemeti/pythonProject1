import Number_Entry as e


def sum_up(number1,number2):
    if number2 < number1:
        print("Not valid interval, the second number is smaller than the first! Try it again!")

    else:
        sum=0
        for x in range(number1, number2+1):
            sum=sum+x
            print(f"+  {x} ")

        print(f"= {sum}")


number1=e.enter_number("number1")
number2=e.enter_number("number2")
sum_up(number1, number2)
