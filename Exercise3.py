


# function asks the name and the age and than print it to the console
def name_age():
 name= input("Enter your name: ")

 while True:
  try:
   age= int(input("Enter your age :"))
   if 0 < age < 201:
    break
   else:
    print("That's not a valid option!Only numbers between 1-200, please!")
  except:
   print("That's not a valid option!Only numbers between 1-200, please!")



 text1= "Hello, "
 text2= ". You are "
 text3= " years old."

 print("Hello, {}. You are {} years old." .format(name.title(), age))
 print(text1+name+text2+str(age)+text3)
 print(f"Hello, {name.upper()}. You are {age} years old.")


name_age()





