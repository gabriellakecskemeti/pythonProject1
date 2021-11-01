def check_string(my_text):
    if my_text.upper().endswith("A") or my_text.upper()[0] == "A":
        return True

my_text=input("Enter a text for checking: ")

if check_string(my_text):
    print("Your text was checked. There is an 'A' on the first or last place!")
else:
    print("Your text was checked. The first and last character is not an 'A'")