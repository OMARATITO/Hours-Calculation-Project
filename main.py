name = input("please enter your name: ")
print(f"hello {name}")

seconds = int(input("please type the number of seconds: "))


hours = seconds // 3600
minutes = seconds % 3600 // 60
the_seconds = seconds % 60

print(f"the hours is {str(hours)} and minutes is {str(minutes)} and seconds is {str(the_seconds)}")
# my Hours Calculation Project