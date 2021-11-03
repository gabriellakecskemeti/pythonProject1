import Number_Entry as e

def triangle(rows):
    x=0
    pattern=""
    for x in range(0,rows):
        pattern = pattern+"*  "
        print(pattern)


my_rows = e.interval_entry(" rows for triangle", 1, 80)

triangle(my_rows)
