# argument is the value that supply the function (nasa calling part/greet_user("")
# parameters are the holes or placeholders that we define in our function for receiving information (nasa def part)

first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
name = ""

def greet_user(name): 
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user(name)
print("Finish")