import Number_Entry as e

def sequence(snum):
    if snum<0 or snum>9:
        print("Number must be between 0 and 9. Please try it again")
    else:
        sequence=""
        i=0
        for i in range(0,10):
            if i != snum:
                sequence = sequence + str(i) + " "

    print(sequence)


takeoff = e.enter_number("number")

sequence(takeoff)